# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0002_auto_20160209_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='mobilenum',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
