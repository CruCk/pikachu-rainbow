# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0004_auto_20160210_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetails',
            old_name='mobilenum',
            new_name='mobilenumber',
        ),
    ]
