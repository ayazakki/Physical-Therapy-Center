# Generated by Django 4.1.7 on 2023-06-24 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0012_remove_maintenance_devicess_maintenance_deevicess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='deevicess',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='deevicess',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='center.device'),
        ),
    ]
