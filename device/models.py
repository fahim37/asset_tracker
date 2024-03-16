from django.db import models

from account.models import Company, Employee


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.company.company_name} - {self.device_type} ({self.serial_number})"
        )


class Checkout(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(auto_now_add=True)
    checked_in_at = models.DateTimeField(blank=True, null=True)
    condition_on_checkout = models.TextField(blank=True)
    condition_on_return = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.device} checked out to {self.employee.name} ({self.checked_out_at})"
        )
