# Generated by Django 4.2.3 on 2023-08-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0004_addmoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoney',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
