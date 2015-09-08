# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards_func(apps, schema_editor):
    HackerNewsItem = apps.get_model("webapp", "HackerNewsItem")
    db_alias = schema_editor.connection.alias
    for i in HackerNewsItem.objects.using(db_alias).all():
        i.comments_new = int(
            0 if not i or i.comments in ["discuss", None] else i.comments.split(" ")[0]
        )
        i.points_new = i.points and int(i.points.split(" ")[0])
        i.save()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20150905_1454'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentItem',
        ),
        migrations.AddField(
            model_name='hackernewsitem',
            name='comments_new',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='hackernewsitem',
            name='points_new',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.RunPython(
            forwards_func,
        ),
    ]
