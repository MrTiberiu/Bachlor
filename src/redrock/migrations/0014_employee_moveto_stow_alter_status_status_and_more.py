# Generated by Django 4.0.2 on 2022-03-19 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redrock', '0013_rename_statustitle_status_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.IntegerField(
                    primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('zipCode', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MoveTo',
            fields=[
                ('moveToID', models.IntegerField(
                    primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stow',
            fields=[
                ('stowID', models.IntegerField(primary_key=True, serialize=False)),
                ('locationStow', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='operation',
            name='assignee',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='redrock.employee'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='moveTo',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='redrock.moveto'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='stow',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='redrock.stow'),
        ),
    ]