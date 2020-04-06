from django.db import models
from django_countries.fields import CountryField

CRITICAL_CHOICES = (
    ('1', 'High'),
    ('2', 'Medium'),
    ('3', 'Low'),
    ('0', 'Unknown')
)


class Company(models.Model):
    name = models.CharField(max_length=200)
    subgroup = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        sorted('name')

    def __str__(self):
        return '{}-{}'.format(self.name, self.subgroup)


class CompanyDetails(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField()

    class Meta:
        sorted('company')

    def __str__(self):
        return '{}'.format(self.company)


class CompanyNumber(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)  # TODO: to be provided by Twilio
    is_whatsapp = models.BooleanField(default=False)
    uri = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        sorted('company')

    def __str__(self):
        return '{}'.format(self.company)


class Category(models.Model):
    category = models.CharField(max_length=200)
    critical = models.CharField(choices=CRITICAL_CHOICES, default='3', max_length=10)
    keywords = models.CharField(max_length=2000, blank=True, null=True, help_text='Add comma seperated keywords for' \
                                                                                  ' better filtering')

    class Meta:
        sorted('critical')

    def __str__(self):
        return '{}'.format(self.category)