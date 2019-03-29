# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class ZhilianPipeline(object):
    def process_item(self, item, spider):
        filename = item['city'] + '.csv'
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            with open(filename, "r") as f:
                reader = csv.reader(f)
                if not [row for row in reader]:  # 判断是否为空表，若为空表，则填入表头
                    writer.writerow(['公司名称', '职位名称', '薪资', '所在城市', '公司所在区域', '工作经验', '学历要求', '招聘人数', '公司福利'])
                    l = [
                        item['companyName'],
                        item['jobName'],
                        item['salary'],
                        item['city'],
                        item['area'],
                        item['workingExp'],
                        item['eduLevel'],
                        item['recruieCount'],
                        item['welfare']
                    ]
                    writer.writerow(l)
                else:
                    l = [
                        item['companyName'],
                        item['jobName'],
                        item['salary'],
                        item['city'],
                        item['area'],
                        item['workingExp'],
                        item['eduLevel'],
                        item['recruieCount'],
                        item['welfare']
                    ]
                    writer.writerow(l)
                    return item

    def close_spider(self, spider):
        print("爬取完毕")
