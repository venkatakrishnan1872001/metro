# Generated by Django 4.2.3 on 2023-08-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0020_remove_cardcreation_otp_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardcreation',
            name='otp_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
