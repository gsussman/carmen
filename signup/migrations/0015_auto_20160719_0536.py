# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0014_auto_20160719_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='shared_with',
            field=models.ManyToManyField(related_name='owner', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
