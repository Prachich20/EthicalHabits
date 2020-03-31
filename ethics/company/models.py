from django.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    country = CountryField()

    class Meta:
        sorted('name')

    def __str__(self):
        return '{}'.format(self.name)
