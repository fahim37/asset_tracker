from rest_framework import serializers
from account.models import Employee, Company


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Employee
        fields = ["email", "name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password do not match"
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2", None)
        if self.context["request"].user.is_authenticated:

            user = self.context["request"].user
            print(user)
            company = user.company
            employee = Employee.objects.create_employee(
                company=company, **validated_data
            )
            return employee

        return super().create(validated_data)


class CompanySerializer(serializers.ModelSerializer):
    employee = EmployeeRegistrationSerializer(write_only=True)

    class Meta:
        model = Company
        fields = ("company_name", "employee")

    def create(self, validated_data):
        employee_data = validated_data.pop("employee")
        company = Company.objects.create(validated_data)
        Employee.objectscreate_employee(company=company, **employee_data)
        return company


class EmployeeLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Employee
        fields = ["email", "password"]


class CompanyDetailSerializer(serializers.Serializer):
    company_name = serializers.CharField()


class EmployeeProfileSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer()

    class Meta:
        model = Employee
        fields = ["company", "id", "email", "name"]
