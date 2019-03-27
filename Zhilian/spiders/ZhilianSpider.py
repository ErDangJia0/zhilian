import scrapy
from ..items import ZhilianItem
import json


class ZhilianSprder(scrapy.Spider):
    name = 'zhilian'
    start = 0
    inputCity = input("请输入你要查询的城市：")
    if inputCity == "北京":
        cityNum = '530'
    elif inputCity == "太原":
        cityNum = '576'
    kw = input("请输入你要查询的职位类型：")
    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&at=5ec2b080c83742439906df02dc91165e&rt=c003e643c2d042f2ab1b3074ca762d11&_v=0.71900858&userCode=1026516348&x-zp-page-request-id=d77497a529f14a85858b66dfea108307-1553049523549-619374&cityId=' + cityNum + '&kw=' + kw + '&start='
    start_urls = [url + str(start)]

    def parse(self, response):
        data = json.loads(response.text)['data']
        numFound = data['numFound']
        result = data['results']
        for info in result:
            positionURL = info['positionURL']
            yield scrapy.Request(url=positionURL, callback=self.getHtml)
        if self.start + 90 < numFound:
            self.start += 90
            yield scrapy.Request(self.url + str(self.start), callback=self.parse)

    def getHtml(self, response):
        item = ZhilianItem()
        item['companyName']=response.xpath("//div[@id='root']/div[@class='a-center-layout__content']//div[@class='company']/a[@class='company__title']/text()").extract()
        item['jobName']=response.xpath("//div[@id='root']/div[@class='job-summary']//h3/text()").extract()
        item['salary']=response.xpath("//div[@id='root']/div[@class='job-summary']//span[@class='summary-plane__salary']/text()").extract()
        item['city']=response.xpath("//div[@id='root']/div[@class='job-summary']//ul[@class='summary-plane__info']/li/a/text()").extract()
        item['workingExp']=response.xpath("//div[@id='root']/div[@class='job-summary']//ul[@class='summary-plane__info']/li/text()")[0].extract()
        item['eduLevel'] = \
        response.xpath("//div[@id='root']/div[@class='job-summary']//ul[@class='summary-plane__info']/li/text()")[
            1].extract()
        item['recruieCount'] = \
        response.xpath("//div[@id='root']/div[@class='job-summary']//ul[@class='summary-plane__info']/li/text()")[
            2].extract()
        yield item

