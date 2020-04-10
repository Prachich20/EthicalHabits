import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ethics.ethics.settings'
import django

django.setup()


from twilio.rest import Client
import ethics.ethics.settings as settings
from sms.models import Sms
from master.models import MasterData

Sms.objects.all().delete()
MasterData.objects.all().delete()

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
# account_sid = settings.ACCOUNT_SID
# auth_token = settings.AUTH_TOKEN
# client = Client(account_sid, auth_token)
#
# smss = Sms.objects.all()
# for sms in smss:
#     client.messages(sms.sid).delete()
#     print(f'deleted {sms.body}')