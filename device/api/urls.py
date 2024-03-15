from django.urls import path
from .views import DeviceListAPIView, DeviceDetailAPIView

urlpatterns = [
    path("", DeviceListAPIView.as_view(), name="device-list"),
    path("<int:pk>/", DeviceDetailAPIView.as_view(), name="device-detail"),
]
