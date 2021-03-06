# Generated by Django 3.0.4 on 2020-04-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_companynumber_uri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('critical', models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low'), ('0', 'Unknown')], default='3', max_length=10)),
                ('keywords', models.CharField(blank=True, help_text='Add comma seperated keywords for better filtering', max_length=2000, null=True)),
            ],
        ),
    ]
