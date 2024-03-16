from django.urls import path
from .views import (
    DeviceListView,
    DeviceDetailView,
    CheckoutListView,
    CheckoutDetailView,
)

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    path("<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("checkouts/", CheckoutListView.as_view(), name="checkout-list"),
    path("checkouts/<int:pk>/", CheckoutDetailView.as_view(), name="checkout-detail"),
]
