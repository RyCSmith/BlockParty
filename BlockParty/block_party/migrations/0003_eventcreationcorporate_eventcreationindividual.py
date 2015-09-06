# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block_party', '0002_event_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCreationCorporate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(to='block_party.CorporateProfile')),
                ('event', models.ForeignKey(to='block_party.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventCreationIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(to='block_party.IndividualProfile')),
                ('event', models.ForeignKey(to='block_party.Event')),
            ],
        ),
    ]
