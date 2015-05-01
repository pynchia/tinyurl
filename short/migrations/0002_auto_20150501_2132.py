# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='num_hits',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='url',
            field=models.URLField(help_text=b'the one you want to shorten'),
        ),
    ]
