# Generated by Django 4.2.3 on 2023-08-05 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0011_rename_phno_buyticket_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyticket',
            name='otp',
        ),
    ]