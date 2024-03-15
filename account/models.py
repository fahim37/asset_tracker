from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.company_name


# Employee manager
class EmployeeManager(BaseUserManager):
    def create_employee(self, company, email, name, password=None, password2=None):
        if not email:
            raise ValueError("Employees must have an email address")

        employee = self.model(
            email=self.normalize_email(email), name=name, company=company
        )

        employee.set_password(password)
        employee.save(using=self._db)
        return employee


class Employee(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upddated_at = models.DateTimeField(auto_now=True)

    object = EmployeeManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "is_admin"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the employee have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the employee have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the employee a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
