# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0003_auto_20150502_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='url',
            field=models.URLField(help_text=b'the URL you want to shorten'),
        ),
    ]
