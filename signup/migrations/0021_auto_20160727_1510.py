# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0020_location_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.URLField(null=True, blank=True),
        ),
    ]
