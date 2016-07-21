# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20160708_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='long',
            new_name='lng',
        ),
        migrations.RemoveField(
            model_name='location',
            name='type',
        ),
    ]
