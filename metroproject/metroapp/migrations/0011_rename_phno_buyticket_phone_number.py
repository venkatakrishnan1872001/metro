# Generated by Django 4.2.3 on 2023-08-05 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metroapp', '0010_rename_area_citylist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyticket',
            old_name='phno',
            new_name='phone_number',
        ),
    ]
