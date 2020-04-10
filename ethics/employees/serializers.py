from rest_framework import serializers
from employees.models import EmployeeDetails, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'company', 'company_admin', 'firstname', 'middlename', 'lastname', 'email']


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = ['id', 'user', 'dob', 'contact_number', 'office _address']
