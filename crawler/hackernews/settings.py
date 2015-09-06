# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hn_clone.settings'

BOT_NAME = 'hackernews'

SPIDER_MODULES = ['crawler.hackernews.spiders']
NEWSPIDER_MODULE = 'crawler.hackernews.spiders'

ITEM_PIPELINES = {
    'crawler.hackernews.pipelines.HackernewsDbStorePipeline': 300,
}

DOWNLOAD_DELAY = 0.5
