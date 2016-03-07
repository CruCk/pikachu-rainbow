# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0006_employeedetails_orderdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regAdminfirstname', models.CharField(default=None, max_length=50)),
                ('regAdminlastname', models.CharField(default=None, max_length=50)),
                ('regAdminusername', models.CharField(unique=True, max_length=20)),
                ('regAdminemail', models.EmailField(unique=True, max_length=254)),
                ('regAdminpassword', models.CharField(max_length=20)),
                ('regAdminmobilenumber', models.CharField(unique=True, max_length=15)),
                ('regAdminaddress', models.CharField(max_length=500)),
            ],
        ),
    ]
