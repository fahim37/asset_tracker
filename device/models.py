from django.db import models
from account.models import Company


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_type = models.TextField()
    serial_number = models.CharField(max_length=255, unique=True)
    condition_on_checkout = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.company.company_name} - {self.device_type} ({self.serial_number})"
        )
