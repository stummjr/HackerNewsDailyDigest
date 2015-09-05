# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem
from webapp import models


class HackerNewsItem(DjangoItem):
    django_model = models.HackerNewsItem
