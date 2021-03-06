# Generated by Django 3.0.8 on 2020-08-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200828_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(help_text='\n    Street address, P.O. box, c/o.\n  ', max_length=30, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='City'),
        ),
    ]
