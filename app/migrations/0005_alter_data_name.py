# Generated by Django 4.1.11 on 2023-09-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_data_high_school_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='NAME',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
