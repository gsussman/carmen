# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0016_auto_20160719_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(default='none', max_length=25, null=True),
        ),
    ]
