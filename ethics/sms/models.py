from django.db import models


class Sms(models.Model):
    sid = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    message_from = models.CharField(max_length=15)
    from_service = models.CharField(max_length=20, blank=True, null=True)
    message_to = models.CharField(max_length=14)
    to_service = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=300)
    direction = models.CharField(max_length=30)
    account_sid = models.CharField(max_length=50)
    created = models.DateTimeField(max_length=100)
    error_code = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        sorted('created')

    def __str__(self):
        return '{}'.format(self.sid)