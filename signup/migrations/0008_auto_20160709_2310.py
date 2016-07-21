# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20160709_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='trips',
            field=models.ManyToManyField(to='signup.Trip', null=True, blank=True),
        ),
    ]
