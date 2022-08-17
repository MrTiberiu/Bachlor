# Generated by Django 4.0.2 on 2022-02-17 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('redrock', '0004_remove_subtask_operationid_remove_subtask_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('operationID', models.IntegerField(primary_key=True, serialize=False)),
                ('assignee', models.CharField(max_length=255)),
                ('dateRegistered', models.DateTimeField(auto_now_add=True)),
                ('timeStart', models.DateTimeField(auto_now_add=True)),
                ('timeFinish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statusID', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('subtaskID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('containerID', models.CharField(max_length=255)),
                ('containerWeightT', models.DecimalField(decimal_places=2, max_digits=6)),
                ('loadSeq', models.IntegerField()),
                ('moveTo', models.CharField(max_length=255)),
                ('stow', models.CharField(max_length=255)),
                ('operationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redrock.operation')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redrock.status')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redrock.status'),
        ),
    ]
