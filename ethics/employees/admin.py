from django.contrib import admin
from employees.models import Employee, EmployeeDetails


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('company', 'company_admin', 'firstname', 'lastname', 'email')
    # readonly_fields = ['user_id']

    # def user_id(self, obj):
    #     return obj.user_id
    # user_id.short_description = 'User'


class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('contact_number', 'office_address')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)