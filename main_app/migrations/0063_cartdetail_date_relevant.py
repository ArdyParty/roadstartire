# Generated by Django 3.0.8 on 2020-10-03 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0062_auto_20201003_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='date_relevant',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date Relevant'),
        ),
    ]
