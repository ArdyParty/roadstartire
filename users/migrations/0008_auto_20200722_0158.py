# Generated by Django 3.0.8 on 2020-07-22 01:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200721_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='discount_ratio',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='tax',
        ),
        migrations.AddField(
            model_name='customuser',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, default=0, help_text='\n    • Percent discount applied to orders (before tax)<br/>\n    • Must be a number from 0.00 to 100.00 (up to 2 decimal places)\n  ', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount (%)'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tax_percent',
            field=models.DecimalField(decimal_places=2, default=13, help_text='\n    Tax percentage applied to orders (defaults to <strong>13%</strong>)\n  ', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Tax (%)'),
        ),
    ]
