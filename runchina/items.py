# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class RunchinaItem(Item):
    _id = Field()
    name = Field()
    addr = Field()
    time = Field()
    website = Field()
