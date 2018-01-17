# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WymusicItem(scrapy.Item):
    rank = scrapy.Field()      # 排名
    title = scrapy.Field()     # 歌名
    duration = scrapy.Field()  # 时长
    author = scrapy.Field()    # 作者