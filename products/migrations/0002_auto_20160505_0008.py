# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 5, 3, 8, 10, 545405, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
