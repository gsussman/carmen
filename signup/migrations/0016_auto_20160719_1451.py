# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0015_auto_20160719_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='owner',
            field=models.ForeignKey(related_name='trips', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
