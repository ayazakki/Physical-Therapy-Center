# Generated by Django 4.1.7 on 2023-06-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0014_remove_maintenance_deevicess_maintenance_deevicess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='deevicess',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='device_name',
            field=models.ManyToManyField(null=True, related_name='main', to='center.device'),
        ),
    ]
