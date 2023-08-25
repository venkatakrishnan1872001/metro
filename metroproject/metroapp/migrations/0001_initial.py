# Generated by Django 4.2.3 on 2023-07-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardCreation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_no', models.CharField(blank=True, max_length=20, null=True)),
                ('phno', models.CharField(blank=True, max_length=20, null=True)),
                ('salutation', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dataofbirth', models.CharField(blank=True, max_length=50, null=True)),
                ('valid_proof_id', models.CharField(blank=True, max_length=50, null=True)),
                ('valid_proof_no', models.CharField(blank=True, max_length=100, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=100, null=True)),
                ('otp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('application_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_no', models.CharField(blank=True, max_length=18, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
