# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainbowapp', '0007_regadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='empfield',
            field=models.CharField(max_length=20, choices=[(b'Electrician', b'electrician'), (b'Cleaning', b'cleaning'), (b'Plumbing', b'plumbing'), (b'Electronics', b'electronics')]),
        ),
    ]
