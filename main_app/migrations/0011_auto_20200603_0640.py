# Generated by Django 3.0.6 on 2020-06-03 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20200603_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='price_each',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, verbose_name='Price per item ($)'),
        ),
    ]
