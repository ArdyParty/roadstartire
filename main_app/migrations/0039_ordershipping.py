# Generated by Django 3.0.8 on 2020-07-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_auto_20200722_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderShipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=50, verbose_name='Company')),
                ('business_phone', models.CharField(blank=True, max_length=30, verbose_name='Phone')),
                ('country_iso', models.CharField(choices=[('CAN', 'Canada'), ('USA', 'United States')], default='CAN', max_length=3, verbose_name='Country')),
                ('province_iso', models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], default='ON', max_length=2, verbose_name='Province')),
                ('city', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('postal_code', models.CharField(blank=True, max_length=30)),
                ('hst_number', models.CharField(blank=True, max_length=30, verbose_name='HST Number')),
            ],
        ),
    ]
