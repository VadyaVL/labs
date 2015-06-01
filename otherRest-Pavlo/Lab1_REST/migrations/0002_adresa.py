# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_REST', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('misto', models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', db_column=b'misto')),
                ('vulicya', models.CharField(max_length=50, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0', db_column=b'vulicya')),
                ('budinok', models.CharField(max_length=50, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbc', db_column=b'budinok')),
            ],
            options={
                'db_table': 'Adresa',
            },
            bases=(models.Model,),
        ),
    ]
