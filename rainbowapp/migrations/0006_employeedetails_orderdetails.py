# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0005_auto_20160210_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empfirstname', models.CharField(default=None, max_length=50)),
                ('emplastname', models.CharField(default=None, max_length=50)),
                ('empusername', models.CharField(unique=True, max_length=20)),
                ('empemail', models.EmailField(unique=True, max_length=254)),
                ('emppassword', models.CharField(max_length=20)),
                ('empmobilenumber', models.CharField(unique=True, max_length=15)),
                ('empaddress', models.CharField(max_length=500)),
                ('empfield', models.CharField(max_length=5, choices=[(b'ELECT', b'electrician'), (b'CLEAN', b'cleaning'), (b'PLUMB', b'plumbing'), (b'LECTR', b'electronics')])),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customerRating', models.IntegerField(default=0)),
                ('employeeRating', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='rainbowapp.CustomerDetails')),
                ('employee', models.ForeignKey(to='rainbowapp.EmployeeDetails')),
            ],
        ),
    ]
