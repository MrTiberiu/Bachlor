# Generated by Django 4.0.2 on 2022-04-30 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redrock', '0015_alter_operation_timefinish'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='assignee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='redrock.employee'),
            preserve_default=False,
        ),
    ]