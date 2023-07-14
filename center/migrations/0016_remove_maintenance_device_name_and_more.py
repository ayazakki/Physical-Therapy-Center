# Generated by Django 4.1.7 on 2023-06-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0015_remove_maintenance_deevicess_maintenance_device_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='device_name',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='device_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='center.device'),
        ),
    ]
