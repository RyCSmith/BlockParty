# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorporateProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=15)),
                ('street_address', models.CharField(max_length=200)),
                ('city_name', models.CharField(max_length=200)),
                ('state_name', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=10)),
                ('business_name', models.CharField(max_length=200)),
                ('contact_first', models.CharField(max_length=200)),
                ('contact_last_name', models.CharField(max_length=200)),
                ('contact_title', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time_of_day', models.CharField(max_length=100, choices=[(b'Morning', b'Morning'), (b'Afternoon', b'Afternoon'), (b'Evening', b'Evening')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(verbose_name=b'date published')),
                ('business_name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('city_name', models.CharField(max_length=200)),
                ('state_name', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=10)),
                ('invited_street_address', models.CharField(max_length=200)),
                ('invited_city_name', models.CharField(max_length=200)),
                ('invited_state_name', models.CharField(max_length=200)),
                ('invited_zip_code', models.CharField(max_length=10)),
                ('radius', models.IntegerField()),
                ('min_attendance', models.IntegerField()),
                ('confirmed_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='IndividualProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=15)),
                ('street_address', models.CharField(max_length=200)),
                ('city_name', models.CharField(max_length=200)),
                ('state_name', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.CharField(max_length=100, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Waiting', b'Waiting')])),
                ('event', models.ForeignKey(to='block_party.Event')),
                ('invitee', models.ForeignKey(to='block_party.IndividualProfile')),
            ],
        ),
        migrations.AddField(
            model_name='availabilityinfo',
            name='date_time',
            field=models.ForeignKey(to='block_party.DateTime'),
        ),
        migrations.AddField(
            model_name='availabilityinfo',
            name='user',
            field=models.ForeignKey(to='block_party.IndividualProfile'),
        ),
    ]
