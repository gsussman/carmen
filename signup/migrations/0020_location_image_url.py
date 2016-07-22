# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0019_delete_emailsignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
