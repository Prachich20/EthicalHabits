from django.contrib import admin
from companyusers.models import CompanyUser


class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'contact_number', 'company_admin')


admin.site.register(CompanyUser, CompanyUserAdmin)