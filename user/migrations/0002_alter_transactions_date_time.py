# Generated by Django 4.2.9 on 2024-01-08 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2024, 1, 8, 13, 16, 33, 293633, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]
