# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20150901_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='comment_id',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commentitem',
            name='hacker_news_item',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commentitem',
            name='parent',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commentitem',
            name='user_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='comments',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='comments_url',
            field=models.URLField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='points',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='since',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='url',
            field=models.URLField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hackernewsitem',
            name='user_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
