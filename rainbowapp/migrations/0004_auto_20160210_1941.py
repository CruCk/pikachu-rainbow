# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0003_auto_20160209_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='firstname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='lastname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='mobilenum',
            field=models.CharField(unique=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='username',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
