from django.contrib import admin
from company.models import Company, CompanyDetails, CompanyNumber, Category


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subgroup')


class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_number', 'email', 'address', 'city', 'country')


class CompanyNumberAdmin(admin.ModelAdmin):
    list_display = ('company', 'number', 'is_whatsapp', 'uri')
    # readonly_fields = ['uri']


class CategoryDataAdmin(admin.ModelAdmin):
    list_display = ('category', 'critical', 'keywords')


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyDetails, CompanyDetailsAdmin)
admin.site.register(CompanyNumber, CompanyNumberAdmin)
admin.site.register(Category, CategoryDataAdmin)