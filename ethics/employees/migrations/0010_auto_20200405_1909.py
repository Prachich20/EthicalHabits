# Generated by Django 3.0.4 on 2020-04-05 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20200405_1904'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='EmployeeDetails',
        ),
    ]