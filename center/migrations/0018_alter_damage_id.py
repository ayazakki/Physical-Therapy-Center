# Generated by Django 4.1.7 on 2023-06-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0017_alter_damage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damage',
            name='id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
