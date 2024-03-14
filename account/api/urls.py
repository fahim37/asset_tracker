from django.urls import path
from account.api.views import (
    EmployeeRegistrationView,
    EmployeeLoginView,
    EmployeeProfileView,
)


urlpatterns = [
    path("register/", EmployeeRegistrationView.as_view(), name="registration"),
    path("login/", EmployeeLoginView.as_view(), name="login"),
    path("profile/", EmployeeProfileView.as_view(), name="profile"),
]
