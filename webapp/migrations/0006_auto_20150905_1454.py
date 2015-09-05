# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20150905_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsitem',
            name='item_set',
            field=models.ForeignKey(to='webapp.HackerNewsItemSet', null=True),
        ),
    ]
