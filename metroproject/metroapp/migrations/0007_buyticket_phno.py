# Generated by Django 4.2.3 on 2023-08-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0006_buyticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyticket',
            name='phno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
