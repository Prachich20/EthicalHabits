from django.contrib import admin
from sms.models import Sms


class SmsAdmin(admin.ModelAdmin):
    list_display = ('sid', 'direction', 'message_from', 'from_service')


admin.site.register(Sms, SmsAdmin)
