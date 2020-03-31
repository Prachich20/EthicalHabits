from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class CompanyUser(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=30)
    company_admin = models.BooleanField(default=False)

    class Meta:
        sorted('created')
