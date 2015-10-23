# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timeslot', '0002_auto_20150808_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='day',
            field=models.CharField(default='Today', max_length=15),
            preserve_default=False,
        ),
    ]
