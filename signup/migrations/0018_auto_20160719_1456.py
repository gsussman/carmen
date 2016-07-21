# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0017_auto_20160719_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
