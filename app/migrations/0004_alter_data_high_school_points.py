# Generated by Django 4.1.3 on 2023-09-10 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_data_lor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='HIGH_SCHOOL_POINTS',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(7)]),
        ),
    ]
