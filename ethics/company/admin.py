from django.contrib import admin
from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'address', 'city', 'country')


admin.site.register(Company, CompanyAdmin)