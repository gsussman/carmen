# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20160709_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(),
        ),
    ]
