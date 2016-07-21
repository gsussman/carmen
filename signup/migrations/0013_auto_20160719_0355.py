# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0012_auto_20160714_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
        migrations.AddField(
            model_name='trip',
            name='owner',
            field=models.ForeignKey(related_name='trip', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='shared_with',
            field=models.ManyToManyField(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
