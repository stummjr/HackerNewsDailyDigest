from django.db import models


class HackerNewsItemSet(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.timestamp)


class HackerNewsItem(models.Model):
    item_set = models.ForeignKey('HackerNewsItemSet', null=True)
    title = models.CharField(null=True, blank=True, max_length=400)
    url = models.URLField(null=True, blank=True, max_length=400)
    points = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
    comments_url = models.URLField(null=True, blank=True, max_length=400)
    user_name = models.CharField(null=True, blank=True, max_length=50)
    since = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return unicode(self.title)
