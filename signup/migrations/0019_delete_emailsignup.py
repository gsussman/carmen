# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0018_auto_20160719_1456'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailSignup',
        ),
    ]
