# Generated by Django 3.0.3 on 2020-07-21 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nalsiwoori', '0004_auto_20200721_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 14, 11, 22, 287632, tzinfo=utc)),
        ),
    ]
