# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_REST', '0003_auto_20150512_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressaG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('City', models.CharField(max_length=50, verbose_name=b'City', db_column=b'City')),
                ('Street', models.CharField(max_length=50, verbose_name=b'Street', db_column=b'Street')),
                ('House', models.CharField(max_length=50, verbose_name=b'House', db_column=b'House')),
            ],
            options={
                'db_table': 'AddressaG',
            },
            bases=(models.Model,),
        ),
    ]
