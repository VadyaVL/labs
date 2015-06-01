# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_REST', '0002_adresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresa',
            name='budinok',
            field=models.CharField(max_length=50, verbose_name=b'House', db_column=b'budinok'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adresa',
            name='misto',
            field=models.CharField(max_length=50, verbose_name=b'City', db_column=b'misto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adresa',
            name='vulicya',
            field=models.CharField(max_length=50, verbose_name=b'Street', db_column=b'vulicya'),
            preserve_default=True,
        ),
    ]
