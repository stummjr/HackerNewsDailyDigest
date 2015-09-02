from __future__ import absolute_import

import os
from celery import task
from scrapy.settings import CrawlerSettings
from scrapy.crawler import CrawlerProcess
from webapp.models import HackerNewsItem, CommentItem
from crawler.hackernews.spiders.hacker_news_spider import HackerNewsSpider


@task()
def crawl():
    settings = CrawlerSettings()
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.hackernews.settings'
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    settings.setmodule(settings_module_path, priority='project')
    crawler = CrawlerProcess(settings)
    # clean the whole db each time it runs, so the app lists only the first 30 news items
    CommentItem.objects.all().delete()
    HackerNewsItem.objects.all().delete()
    crawler.crawl(HackerNewsSpider)
    crawler.start()
    return 0
