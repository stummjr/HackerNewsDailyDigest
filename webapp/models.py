from django.db import models


class HackerNewsItem(models.Model):
    title = models.CharField(null=True, blank=True, max_length=400)
    url = models.CharField(null=True, blank=True, max_length=400)
    points = models.CharField(null=True, blank=True, max_length=400)
    comments = models.CharField(null=True, blank=True, max_length=400)
    comments_url = models.CharField(null=True, blank=True, max_length=400)
    user_name = models.CharField(null=True, blank=True, max_length=400)
    since = models.CharField(null=True, blank=True, max_length=400)

    def __unicode__(self):
        return unicode(self.title)


class CommentItem(models.Model):
    hacker_news_item = models.CharField(null=True, blank=True, max_length=400)
    comment_id = models.CharField(null=True, blank=True, max_length=400)
    nesting_level = models.IntegerField(null=True, blank=True)
    parent = models.CharField(null=True, blank=True, max_length=400)
    text = models.CharField(null=True, blank=True, max_length=400)
    user_name = models.CharField(null=True, blank=True, max_length=400)

    def __unicode__(self):
        return unicode(self.user_name)
