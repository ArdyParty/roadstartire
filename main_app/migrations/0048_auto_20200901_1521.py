# Generated by Django 3.0.8 on 2020-09-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0047_auto_20200828_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tire',
            name='load',
        ),
        migrations.AddField(
            model_name='tire',
            name='load_speed',
            field=models.CharField(blank=True, max_length=30, verbose_name='Load Index / Speed Rating'),
        ),
    ]
