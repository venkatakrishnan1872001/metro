# Generated by Django 4.2.3 on 2023-08-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0007_buyticket_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='otp_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
