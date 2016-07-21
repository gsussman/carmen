# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='google_id',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='long',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.CharField(default='gene', max_length=250),
            preserve_default=False,
        ),
    ]
