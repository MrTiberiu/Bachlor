# Generated by Django 4.0.2 on 2022-02-17 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redrock', '0012_rename_status_status_statustitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='statusTitle',
            new_name='status',
        ),
    ]
