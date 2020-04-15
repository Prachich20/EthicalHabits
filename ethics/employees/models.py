from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    company_admin = models.BooleanField(default=False)

    firstname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        sorted('company')

    def __str__(self):
        return '{}.{}-{}'.format(self.firstname, self.lastname, (self.company.name, 'admin' if self.company_admin else
            'not admin'))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        is_employee = Employee.objects.filter(email=self.email, ).first()
        if not is_employee:
            user = User()
            user.first_name = self.firstname
            user.last_name = self.lastname
            user.username = ('{}.{}'.format(self.firstname, self.lastname)).lower()
            user.email = self.email
            user.is_staff = True
            user.is_active = True
            user.is_superuser = False
            import ethics.settings as settings
            user.set_password(settings.DEFAULT_PWD)
            user.save()
        else:
            is_user = User.objects.filter(email=is_employee.email).first()
            is_user.email = self.email
            is_user.first_name = self.firstname
            is_user.last_name = self.lastname
            is_user.save()
        # self.is_user = user
        super().save()


class EmployeeDetails(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)

    dob = models.DateField(blank=True, null=True)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    office_address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        sorted('user')

    def __str__(self):
        return '{}'.format(self.user)
