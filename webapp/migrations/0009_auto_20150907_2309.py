# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20150907_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hackernewsitem',
            old_name='comments_new',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='hackernewsitem',
            old_name='points_new',
            new_name='points',
        ),
    ]
