# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    place = scrapy.Field()    #爬取链家租房信息的-地点
    size = scrapy.Field()     #爬取链家租房信息的-房屋平米数
    price = scrapy.Field()  # 爬取链家租房信息的-价格

