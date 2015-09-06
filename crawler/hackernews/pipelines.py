# -*- coding: utf-8 -*-


class HackernewsDbStorePipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
