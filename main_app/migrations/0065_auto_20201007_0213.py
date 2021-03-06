# Generated by Django 3.0.8 on 2020-10-07 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0064_auto_20201003_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '🛒 Cart & Order', 'verbose_name_plural': '🛒 Carts & Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartdetail',
            options={'verbose_name': '🛒📦 Cart Item'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': '📷 Image', 'verbose_name_plural': '📷 Images'},
        ),
        migrations.AlterModelOptions(
            name='ordershipping',
            options={'verbose_name': '📦 Shipping Info', 'verbose_name_plural': '📦 Shipping Info'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '⭐️ Product', 'verbose_name_plural': '⭐️ Products'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': '🚚 Stock', 'verbose_name_plural': '🚚 Stock'},
        ),
        migrations.AlterModelOptions(
            name='tire',
            options={'verbose_name': '📜 Tire History', 'verbose_name_plural': '📜 Tire History'},
        ),
        migrations.AlterModelOptions(
            name='tread',
            options={'verbose_name': '📷 Tread Category & Images', 'verbose_name_plural': '📷 Tread Categories & Images'},
        ),
        migrations.RemoveConstraint(
            model_name='cart',
            name='unique_current_cart',
        ),
        migrations.AlterField(
            model_name='tire',
            name='date_effective',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='\n    The date and time when these changes will come into effect\n  ', verbose_name='Date Effective'),
        ),
    ]
