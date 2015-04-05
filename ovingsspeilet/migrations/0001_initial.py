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
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='tittel')),
                ('description', models.TextField(max_length=10000, blank=True, verbose_name='beskrivelse')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField(verbose_name='starttidspunkt')),
                ('date_end', models.DateField(verbose_name='sluttidspunkt')),
                ('weekly', models.BooleanField(help_text='Repeter ukentlig.', default=False, verbose_name='ukentlig')),
                ('admin_event', models.BooleanField(help_text='Kan kun endres av en admin.', default=False, verbose_name='adminaktivitet')),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='opprettet av')),
            ],
            options={
                'verbose_name_plural': 'aktiviteter',
                'verbose_name': 'aktivitet',
            },
        ),
    ]
