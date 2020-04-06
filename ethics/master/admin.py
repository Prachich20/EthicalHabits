from django.contrib import admin
from master.models import MasterData


class MasterDataAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'location', 'date_received', 'country', 'category', 'critical', 'contact_num')
    readonly_fields = ['company', 'name', 'country', 'category', 'critical', 'contact_num']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(MasterData, MasterDataAdmin)