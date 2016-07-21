# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20160708_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='long',
            field=models.BigIntegerField(),
        ),
    ]
