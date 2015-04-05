# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovingsspeilet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(verbose_name='sluttidspunkt'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(verbose_name='starttidspunkt'),
        ),
    ]
