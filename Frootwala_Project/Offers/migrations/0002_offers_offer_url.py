# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='offer_url',
            field=models.URLField(default=datetime.datetime(2015, 6, 22, 17, 48, 4, 511000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
