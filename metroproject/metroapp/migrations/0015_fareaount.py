# Generated by Django 4.2.3 on 2023-08-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0014_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='FareAount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('fare_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
