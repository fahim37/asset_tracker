from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from account.renderer import EmployeeRenderer
from account.api.serializers import (
    EmployeeRegistrationSerializer,
    EmployeeLoginSerializer,
    EmployeeProfileSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# generate token manually
def get_tokens_for_employee(employee):
    refresh = RefreshToken.for_user(employee)

    return {
        "Access Token": str(refresh.access_token),
        "Refresh Token": str(refresh),
    }


class EmployeeRegistrationView(APIView):
    renderer_classes = [EmployeeRenderer]

    def post(self, request, format=None):
        serializer = EmployeeRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            employee = serializer.save()
            token = get_tokens_for_employee(employee)
            return Response(
                {"token": token, "msg": "Registration Successfull"},
                status=status.HTTP_201_CREATED,
            )


class EmployeeLoginView(APIView):
    renderer_classes = [EmployeeRenderer]

    def post(self, request, format=None):
        serializer = EmployeeLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            employee = authenticate(email=email, password=password)

            if employee is not None:
                token = get_tokens_for_employee(employee)
                return Response(
                    token,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["Email or password is not valid"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )


class EmployeeProfileView(APIView):
    renderer_classes = [EmployeeRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = EmployeeProfileSerializer(request.employee)

        return Response(serializer.data, status=status.HTTP_200_OK)
