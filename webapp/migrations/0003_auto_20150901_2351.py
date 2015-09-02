# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20150901_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
