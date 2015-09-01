# -*- coding: utf-8 -*-
import logging


class HackernewsPipeline(object):
    def process_item(self, item, spider):
        logging.debug("saving to django db: " + str(item))
        item.save()
        return item
