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


class ReturnDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["checked_in_at", "condition_on_return"]
