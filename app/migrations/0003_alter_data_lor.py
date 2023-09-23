# Generated by Django 4.1.3 on 2023-09-10 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_probability_data_high_school_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='LOR',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
