from rest_framework import serializers
from device.models import Device, Checkout


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
