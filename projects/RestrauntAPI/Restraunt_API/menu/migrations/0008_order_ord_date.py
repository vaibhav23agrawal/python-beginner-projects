# Generated by Django 3.2.7 on 2022-06-01 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ord_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 20, 52, 56, 6524)),
        ),
    ]
