# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('mobile_num', models.CharField(max_length=15)),
                ('user_name', models.CharField(max_length=50)),
                ('total_amt', models.CharField(max_length=10)),
                ('del_day', models.CharField(max_length=10)),
                ('del_time', models.CharField(max_length=15)),
                ('flat_no', models.CharField(max_length=10)),
                ('building_name', models.CharField(max_length=40)),
                ('locality_name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='orderitems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('prod_name', models.CharField(max_length=40)),
                ('prod_count', models.CharField(max_length=10)),
                ('prod_base_qty', models.CharField(max_length=20)),
                ('prod_price', models.CharField(max_length=10)),
            ],
        ),
    ]
