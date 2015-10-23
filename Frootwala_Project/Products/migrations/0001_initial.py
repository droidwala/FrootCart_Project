# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(serialize=False, primary_key=True)),
                ('prod_name', models.CharField(max_length=30)),
                ('prod_price', models.IntegerField()),
                ('prod_type', models.CharField(max_length=10)),
                ('prod_qty', models.CharField(max_length=10)),
                ('prod_img_url', models.URLField()),
            ],
        ),
    ]
