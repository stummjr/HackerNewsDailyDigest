# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20150902_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackerNewsItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='hackernewsitem',
            name='item_set',
            field=models.ForeignKey(to='webapp.HackerNewsItem', null=True),
        ),
    ]
