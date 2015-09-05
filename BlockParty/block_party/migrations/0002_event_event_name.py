# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block_party', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_name',
            field=models.CharField(default=b'event', max_length=200),
        ),
    ]
