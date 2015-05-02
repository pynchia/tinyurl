# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_auto_20150501_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='url',
            field=models.URLField(help_text=b'the link you want to shorten', unique=True),
        ),
    ]
