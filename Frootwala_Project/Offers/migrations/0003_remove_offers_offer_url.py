# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Offers', '0002_offers_offer_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='offer_url',
        ),
    ]
