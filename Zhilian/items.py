# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyName = scrapy.Field()  # 公司名称
    jobName = scrapy.Field()  # 职位名称
    salary = scrapy.Field()  # 薪资
    city = scrapy.Field()  # 工作地点
    workingExp = scrapy.Field()  # 工作经验
    eduLevel = scrapy.Field()  # 学历要求
    recruieCount = scrapy.Field()  # 招聘人数
