# Generated by Django 2.2.6 on 2019-10-19 01:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0002_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='article',
            name='shoe_size',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 1, 5, 1, 823592, tzinfo=utc)),
        ),
    ]
