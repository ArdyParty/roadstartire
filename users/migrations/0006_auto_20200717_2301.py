# Generated by Django 3.0.8 on 2020-07-17 23:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200717_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='discount_ratio',
            field=models.DecimalField(decimal_places=2, default=0, help_text='\n    • Discount ratio applied to orders<br/>\n    • Must be a number from 0.00 to 1.00 (up to 2 decimal places)\n  ', max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Discount'),
        ),
    ]
