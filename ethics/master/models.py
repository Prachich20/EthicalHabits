from django.db import models
from company.models import Company
from sms.models import Sms


class MasterData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sms = models.ForeignKey(Sms, on_delete=models.CASCADE)

    name = models.CharField(max_length=800)
    body = models.CharField(max_length=800)
    location = models.CharField(max_length=800)
    country = models.CharField(max_length=800)
    category = models.CharField(max_length=800, blank=True, null=True)
    critical = models.CharField(max_length=800, blank=True, null=True)

    sid = models.CharField(max_length=50)
    contact_num = models.CharField(max_length=15)
    contact_service = models.CharField(max_length=20, blank=True, null=True)
    message_to = models.CharField(max_length=14)
    to_service = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=30)
    status = models.CharField(max_length=300)
    account_sid = models.CharField(max_length=50)
    date_received = models.DateTimeField(max_length=100)

    class Meta:
        sorted('date_received')

    def __str__(self):
        return '{}'.format(self.name)
