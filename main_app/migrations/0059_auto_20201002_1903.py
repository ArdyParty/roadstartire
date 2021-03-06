# Generated by Django 3.0.8 on 2020-10-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0058_auto_20200930_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity_change_type',
            field=models.CharField(choices=[('➕ Increase stock', (('stock received', '🚚 Stock received'),)), ('➖ Decrease stock', (('sold', '💰 \u200dSold Offline'), ('lost', '🤷\u200d♂️ Lost'), ('other', '❓ Other')))], default='stock received', max_length=30, verbose_name='Increase/Decrease Stock'),
        ),
    ]
