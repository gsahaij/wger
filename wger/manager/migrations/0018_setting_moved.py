# Generated by Django 4.2.6 on 2024-04-19 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_alter_workoutlog_exercise_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='moved',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1500)], verbose_name='Weight-Moved'),
        ),
    ]
