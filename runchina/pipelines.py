# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from items import RunchinaItem

class RunchinaPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1',27017)
        db = client['Crawl']
        self.marathon = db['Marathon']

    def process_item(self, item, spider):
        if isinstance(item,RunchinaItem):
            try:
                self.marathon.insert(dict(item))
            except Exception as e:
                pass
