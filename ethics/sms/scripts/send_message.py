import ethics.ethics.settings as settings
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12058464908',
                              body='this is the test message from Prachi',
                              to='+61401179268'
                          )
print(f"message for {message.sid} is sent.")