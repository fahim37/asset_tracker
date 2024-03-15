from rest_framework import serializers
from account.models import Employee, Company


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Employee
        fields = ["company", "email", "name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password do not match"
            )
        return attrs

    def create(self, validated_data):
        company = validated_data.pop("company")
        return Employee.object.create_employee(company=company, **validated_data)


class EmployeeLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Employee
        fields = ["email", "password"]


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "email", "name"]


class CompanySerializer(serializers.ModelSerializer):
    employee = EmployeeRegistrationSerializer()

    class Meta:
        model = Company
        fields = ("company_name", "employee")

    def create(self, validated_data):
        employee_data = validated_data.pop("employee")
        company = Company.objects.create(**validated_data)
        Employee.object.create_employee(company=company, **employee_data)
        return company
