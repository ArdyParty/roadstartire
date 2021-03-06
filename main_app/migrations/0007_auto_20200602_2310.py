# Generated by Django 3.0.6 on 2020-06-02 23:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200602_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='discount_ratio_applied',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="\n    Must be a number from 0.00 to 1.00 (up to 2 decimal places).<br/>\n    Takes the user's discount ratio when the order is submitted.\n  ", max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]
