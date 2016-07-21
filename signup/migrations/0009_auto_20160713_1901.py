# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0008_auto_20160709_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='trips',
            field=models.ManyToManyField(to='signup.Trip', blank=True),
        ),
    ]
