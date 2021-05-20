# -*- coding: utf-8 -*-

import scrapy


class CubeeItem(scrapy.Item):
    filename = scrapy.Field()
    rsp = scrapy.Field()
    images = scrapy.Field()
