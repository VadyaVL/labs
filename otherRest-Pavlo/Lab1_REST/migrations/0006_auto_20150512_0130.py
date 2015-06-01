# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_REST', '0005_auto_20150512_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbitrazhnij',
            name='Adresa',
        ),
        migrations.RemoveField(
            model_name='borzhnik',
            name='Adresa',
        ),
        migrations.RemoveField(
            model_name='borzhnik',
            name='Arbitrazh',
        ),
        migrations.DeleteModel(
            name='Arbitrazhnij',
        ),
        migrations.RemoveField(
            model_name='kreditor',
            name='Adresa',
        ),
        migrations.DeleteModel(
            name='Adresa',
        ),
        migrations.RemoveField(
            model_name='vimogi',
            name='Borzhnik',
        ),
        migrations.DeleteModel(
            name='Borzhnik',
        ),
        migrations.RemoveField(
            model_name='vimogi',
            name='Kreditor',
        ),
        migrations.DeleteModel(
            name='Kreditor',
        ),
        migrations.DeleteModel(
            name='Vimogi',
        ),
    ]
