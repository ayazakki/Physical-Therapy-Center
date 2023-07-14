# Generated by Django 4.1.7 on 2023-06-24 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0008_alter_device_deviceid_alter_patient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damage',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='dam',
        ),
        migrations.RemoveField(
            model_name='device',
            name='maintenance',
        ),
        migrations.AddField(
            model_name='damage',
            name='Devicess',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Device', to='center.device'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='device_name',
            field=models.ManyToManyField(related_name='main', to='center.device'),
        ),
    ]