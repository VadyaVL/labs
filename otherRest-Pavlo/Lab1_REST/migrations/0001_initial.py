# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('City', models.CharField(max_length=50, verbose_name=b'City', db_column=b'City')),
                ('Street', models.CharField(max_length=50, verbose_name=b'Street', db_column=b'Street')),
                ('House', models.CharField(max_length=50, verbose_name=b'House', db_column=b'House')),
                ('Phone', models.CharField(max_length=50, verbose_name=b'Phone', db_column=b'Phone')),
            ],
            options={
                'db_table': 'Address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'Name', db_column=b'Name')),
                ('DateReg', models.DateField(verbose_name=b'DateReg', db_column=b'DateReg')),
                ('Address', models.ForeignKey(to='Lab1_REST.Address')),
            ],
            options={
                'db_table': 'Filia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormOfLeg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'Name', db_column=b'Name')),
            ],
            options={
                'db_table': 'FormOfLeg',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'Name', db_column=b'Name')),
                ('Surname', models.CharField(max_length=50, verbose_name=b'Surname', db_column=b'Surname')),
                ('Phone', models.CharField(max_length=50, verbose_name=b'Phone', db_column=b'Phone')),
            ],
            options={
                'db_table': 'Person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialFormation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'Name', db_column=b'Name')),
                ('DateReg', models.DateField(verbose_name=b'DateReg', db_column=b'DateReg')),
                ('RegNumb', models.IntegerField(verbose_name=b'RegNumb', db_column=b'RegNumb')),
                ('Address', models.ForeignKey(to='Lab1_REST.Address')),
                ('FormOfLeg', models.ForeignKey(to='Lab1_REST.FormOfLeg')),
                ('Person', models.ForeignKey(to='Lab1_REST.Person')),
            ],
            options={
                'db_table': 'SocialFormation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeOfSocForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'Name', db_column=b'Name')),
            ],
            options={
                'db_table': 'TypeOfSocForm',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='socialformation',
            name='TypeOfSocForm',
            field=models.ForeignKey(to='Lab1_REST.TypeOfSocForm'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filia',
            name='Person',
            field=models.ForeignKey(to='Lab1_REST.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filia',
            name='SocialFormation',
            field=models.ForeignKey(to='Lab1_REST.SocialFormation'),
            preserve_default=True,
        ),
    ]
