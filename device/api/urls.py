from django.urls import path

from .views import (
    DeviceListView,
    DeviceDetailView,
    CheckoutListView,
    CheckoutDetailView,
    DeviceReturnView,
)

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    path("<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("checkout/", CheckoutListView.as_view(), name="checkout-list"),
    path("checkout/<int:pk>/", CheckoutDetailView.as_view(), name="checkout-detail"),
    path("checkout/return/<int:pk>/", DeviceReturnView.as_view(), name="return-device"),
]
