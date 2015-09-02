# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hacker_news_item', models.CharField(max_length=400)),
                ('comment_id', models.CharField(max_length=400)),
                ('nesting_level', models.IntegerField()),
                ('parent', models.CharField(max_length=400)),
                ('text', models.CharField(max_length=400)),
                ('user_name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='HackerNewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('url', models.CharField(max_length=400)),
                ('points', models.CharField(max_length=400)),
                ('comments', models.CharField(max_length=400)),
                ('comments_url', models.CharField(max_length=400)),
                ('user_name', models.CharField(max_length=400)),
                ('since', models.CharField(max_length=400)),
            ],
        ),
    ]
