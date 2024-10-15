# Generated by Django 5.0.6 on 2024-06-27 22:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='HIGH_SCHOOL_POINTS',
        ),
        migrations.RemoveField(
            model_name='data',
            name='LOR',
        ),
        migrations.RemoveField(
            model_name='data',
            name='NAME',
        ),
        migrations.RemoveField(
            model_name='data',
            name='RCN',
        ),
        migrations.RemoveField(
            model_name='data',
            name='SOP',
        ),
        migrations.RemoveField(
            model_name='data',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='data',
            name='TOEFL',
        ),
        migrations.RemoveField(
            model_name='data',
            name='UGPA',
        ),
        migrations.AddField(
            model_name='data',
            name='Age_month',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='data',
            name='Age_of_mom',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='BMI_of_mom',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Food_group_consumed',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='data',
            name='Food_intake_per_day',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Height_in_cm',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Height_of_mom',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='No_of_Children_ever_born',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Sex',
            field=models.PositiveIntegerField(choices=[(1, 'Male'), (0, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Weight_kg',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='Weight_of_mom_in_kg',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='malnutrition_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='mother_status',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='data',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
