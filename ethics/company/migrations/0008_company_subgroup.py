# Generated by Django 3.0.4 on 2020-04-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='subgroup',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]