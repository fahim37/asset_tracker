from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from device.models import Device, Checkout
from .serializers import DeviceSerializer, CheckoutSerializer, ReturnDeviceSerializer
from django.shortcuts import get_object_or_404


class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Device, pk=pk)

    def get(self, request, pk):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        device = self.get_object(pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckoutListView(APIView):
    def get(self, request):
        checkouts = Checkout.objects.all()
        serializer = CheckoutSerializer(checkouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Update the checked_out field of the Device
            device_id = request.data.get("device")
            device = get_object_or_404(Device, pk=device_id)
            device.checked_out = True
            device.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckoutDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Checkout, pk=pk)

    def get(self, request, pk):
        checkout = self.get_object(pk)
        serializer = CheckoutSerializer(checkout)
        return Response(serializer.data)

    def put(self, request, pk):
        checkout = self.get_object(pk)
        serializer = CheckoutSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checkout = self.get_object(pk)
        checkout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceReturnView(APIView):
    def post(self, request, pk):
        checkout = get_object_or_404(Checkout, pk=pk)
        serializer = ReturnDeviceSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Update the checked_out field of the Device
            checkout.device.checked_out = False
            checkout.device.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
