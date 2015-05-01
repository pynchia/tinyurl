# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(help_text=b'URL')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('num_hits', models.IntegerField(editable=False)),
            ],
        ),
    ]
