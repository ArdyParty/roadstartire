# Generated by Django 3.0.6 on 2020-06-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200625_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.IntegerField(choices=[(0, 'Current'), (1, 'In Progress'), (2, 'Cancelled'), (3, 'Fulfilled'), (-1, 'Abandoned')], help_text="\n    <br/>\n    A Cart can be in 1 of 5 states:<br/>\n    1. <strong>Current</strong> - The currently open cart (each user can only have 1 cart in this state)<br/>\n    2. <strong>Abandoned</strong> - The last item in the cart was removed or the cart timeout was reached<br/>\n    3. <strong>In progress</strong> - Cart has been submitted but not yet fulfilled nor cancelled<br/>\n    4. <strong>Cancelled</strong> - Cart can no longer be fulfilled<br/>\n    5. <strong>Fulfilled</strong> - Items have been delivered to client and payment has been received<br/>\n\n    <br/>\n    <strong>NOTE: </strong>A Cart's status must only ever progress forwards\n  "),
        ),
    ]