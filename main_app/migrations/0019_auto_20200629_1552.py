# Generated by Django 3.0.6 on 2020-06-29 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20200626_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Created (UTC)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Modified (UTC)'),
        ),
    ]
