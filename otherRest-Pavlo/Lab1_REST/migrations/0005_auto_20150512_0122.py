# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_REST', '0004_addressag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitrazhnij',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prizvishhe', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', db_column=b'prizvishhe')),
                ('imya', models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', db_column=b'imya')),
                ('po_batkovi', models.CharField(max_length=50, verbose_name=b'\xd0\x9e\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', db_column=b'po_batkovi')),
                ('nomer', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80', db_column=b'nomer')),
                ('data_vidachi', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_column=b'data_vidachi')),
                ('telefon', models.CharField(max_length=50, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', db_column=b'telefon')),
                ('Adresa', models.ForeignKey(to='Lab1_REST.Adresa')),
            ],
            options={
                'db_table': 'Arbitrazhnij',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Borzhnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('najmenuvannya', models.CharField(max_length=50, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', db_column=b'najmenuvannya')),
                ('kod_edrpou', models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\x95\xd0\x94\xd0\xa0\xd0\x9f\xd0\x9e\xd0\xa3', db_column=b'kod_edrpou')),
                ('prizvishhe', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', db_column=b'prizvishhe')),
                ('imya', models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', db_column=b'imya')),
                ('po_batkovi', models.CharField(max_length=50, verbose_name=b'\xd0\x9e\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', db_column=b'po_batkovi')),
                ('nomer_edryuofop', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\x95\xd0\x94\xd0\xa0\xd0\xae\xd0\x9e\xd0\xa4\xd0\x9e\xd0\x9f', db_column=b'nomer_edryuofop')),
                ('vid_diyalnosti', models.CharField(max_length=50, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd0\xb4\xd0\xb5\xd1\x8f\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8', db_column=b'vid_diyalnosti')),
                ('forma_vlasnosti', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb1\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8', db_column=b'forma_vlasnosti')),
                ('chastka_derzhavi', models.CharField(max_length=50, verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c \xd0\xb3\xd0\xbe\xd1\x81\xd1\x83\xd0\xb4\xd0\xb0\xd1\x80\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0', db_column=b'chastka_derzhavi')),
                ('data_porush_provadzh', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb1\xd1\x83\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0', db_column=b'data_porush_provadzh')),
                ('stan_provadzhennya', models.CharField(max_length=50, verbose_name=b'\xd0\xa1\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0', db_column=b'stan_provadzhennya')),
                ('Adresa', models.ForeignKey(to='Lab1_REST.Adresa')),
                ('Arbitrazh', models.ForeignKey(to='Lab1_REST.Arbitrazhnij')),
            ],
            options={
                'db_table': 'Borzhnik',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kreditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prizvishhe', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', db_column=b'prizvishhe')),
                ('imya', models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', db_column=b'imya')),
                ('po_batkovi', models.CharField(max_length=50, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', db_column=b'po_batkovi')),
                ('nomer_edryuofop', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\x95\xd0\x94\xd0\xa0\xd0\xae\xd0\x9e\xd0\xa4\xd0\x9e\xd0\x9f', db_column=b'nomer_edryuofop')),
                ('telefon', models.CharField(max_length=50, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', db_column=b'telefon')),
                ('Adresa', models.ForeignKey(to='Lab1_REST.Adresa')),
            ],
            options={
                'db_table': 'Kreditor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vimogi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zagalna_suma', models.IntegerField(verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb0\xd1\x8f \xd1\x81\xd1\x83\xd0\xbc\xd0\xb0', db_column=b'zagalna_suma')),
                ('viplacheno', models.IntegerField(verbose_name=b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe', db_column=b'viplacheno')),
                ('kinceva_data', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8b', db_column=b'kinceva_data')),
                ('Borzhnik', models.ForeignKey(to='Lab1_REST.Borzhnik')),
                ('Kreditor', models.ForeignKey(to='Lab1_REST.Kreditor')),
            ],
            options={
                'db_table': 'Vimogi',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='AddressaG',
        ),
        migrations.AlterField(
            model_name='adresa',
            name='budinok',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbc', db_column=b'budinok'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adresa',
            name='misto',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', db_column=b'misto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adresa',
            name='vulicya',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0', db_column=b'vulicya'),
            preserve_default=True,
        ),
    ]
