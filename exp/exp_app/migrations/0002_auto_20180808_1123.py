# Generated by Django 2.0.7 on 2018-08-08 05:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 5, 53, 40, 242725, tzinfo=utc)),
        ),
    ]
