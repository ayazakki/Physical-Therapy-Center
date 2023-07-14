# Generated by Django 4.2 on 2023-06-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0019_alter_treatment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='Max_number_per_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Responsible_party',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]