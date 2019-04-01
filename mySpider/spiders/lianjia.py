import scrapy
from scrapy.http import Request
from mySpider.items import LianjiaItem
import re


class LianJiaSpider(scrapy.Spider):
    #  必须继承scrapy.Spider

    name = "lianjia"   # 名称
    start_urls = ['https://nb.lianjia.com/zufang/yinzhouqu2/pg1/']   # URL列表
    allowed_domains = ["lianjia.com"]

    def parse(self, response):
        match_number = '\d+㎡'
        infos = response.xpath('//div[@class="content__list--item--main"]')

        # 地点 平米 content__list - -item - -des
        # content__list - -item - price

        for info in infos:
            item = LianjiaItem()
            # 获取地点
            try:
                place = info.xpath('p[@class="content__list--item--des"]/a/text()').extract()[0] + info.xpath('p[@class="content__list--item--des"]/a/text()').extract()[1]
            except Exception:
                place = '找不到地点'
            # 获取平米数
            try:
                size = re.findall(match_number, info.xpath('p[@class="content__list--item--des"]/text()').extract()[3])
                size = size[0]
            except Exception:
                size = '找不到大小'
                pass

            # 获取价格
            price = info.xpath('span[@class="content__list--item-price"]/em/text()').extract()[0]

            item['place'] = place
            item['size'] = size
            item['price'] = price

            yield item   # 返回数据

        # 从新设置URL，从第2页到第100页  回调parse方法
        for i in range(2, 4):
            url = 'https://nb.lianjia.com/zufang/yinzhouqu2/pg{}/'.format(str(i))
            yield Request(url, callback=self.parse)  # 回调
