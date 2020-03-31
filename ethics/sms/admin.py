from django.contrib import admin
from sms.models import Sms


class SmsAdmin(admin.ModelAdmin):
    list_display = ('sid', 'message_from', 'message_to', 'from_service', 'direction', 'status', 'created')
    readonly_fields = ['sid', 'body', 'message_from', 'from_service', 'message_to', 'to_service', 'direction',
                       'url', 'direction', 'status', 'created', 'error_code', 'error_message', 'account_sid']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Sms, SmsAdmin)
