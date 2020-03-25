import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ethics.settings'
import django
django.setup()
import ethics.settings as settings
from twilio.rest import Client

from sms.models import Sms

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)
all_sms = Sms.objects.all()


def load():
    messages = client.messages.list()
    for record in messages:
        sms = all_sms.filter(sid=record.sid).first()
        if not sms:
            from_ = record.from_.split(':')
            from_num = from_[0] if len(from_) == 1 else from_[1]
            from_service = '' if len(from_) == 1 else from_[0]

            to_ = record.to.split(':')
            to_num = from_[0] if len(to_) == 1 else to_[1]
            to_service = '' if len(to_) == 1 else to_[0]

            new_sms = Sms()
            new_sms.sid = record.sid
            new_sms.message_to = to_num
            new_sms.to_service = to_service
            new_sms.message_from = from_num
            new_sms.from_service = from_service
            new_sms.account_sid = account_sid
            new_sms.direction = record.direction
            new_sms.error_message = record.error_message
            new_sms.error_code = record.error_code
            new_sms.body = record.body
            new_sms.created = record.date_created
            new_sms.save()
            print(f"record created for {new_sms.sid}")

if __name__ == '__main__':
    load()
