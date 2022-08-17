# Generated by Django 4.0.2 on 2022-02-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redrock', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='timeFinish',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='timeStart',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='moveTo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='stow',
            field=models.CharField(max_length=255, null=True),
        ),
    ]