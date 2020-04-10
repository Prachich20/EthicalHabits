from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from employees.serializers import EmployeeSerializer, EmployeeDetailsSerializer
from employees.models import Employee, EmployeeDetails


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'company_admin', 'firstname', 'middlename', 'lastname', 'email']


class EmployeeDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'dob', 'contact_number', 'office_address']