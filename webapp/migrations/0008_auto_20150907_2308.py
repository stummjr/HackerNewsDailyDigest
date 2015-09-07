# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20150907_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackernewsitem',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='hackernewsitem',
            name='points',
        ),
    ]
