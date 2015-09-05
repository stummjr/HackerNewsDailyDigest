from django.db import models


class HackerNewsItemSet(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)


class HackerNewsItem(models.Model):
    # TODO: remove null=True
    item_set = models.ForeignKey('HackerNewsItemSet', null=True)
    title = models.CharField(null=True, blank=True, max_length=400)
    url = models.URLField(null=True, blank=True, max_length=400)
    points = models.CharField(null=True, blank=True, max_length=50)
    comments = models.CharField(null=True, blank=True, max_length=50)
    comments_url = models.URLField(null=True, blank=True, max_length=400)
    user_name = models.CharField(null=True, blank=True, max_length=50)
    since = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return unicode(self.title)


class CommentItem(models.Model):
    hacker_news_item = models.CharField(null=True, blank=True, max_length=100)
    comment_id = models.CharField(null=True, blank=True, max_length=50)
    nesting_level = models.IntegerField(null=True, blank=True)
    parent = models.CharField(null=True, blank=True, max_length=100)
    text = models.TextField(null=True, blank=True)
    user_name = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return unicode(self.user_name)
