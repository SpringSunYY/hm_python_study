import scrapy
from items import ItcItem


class SunoneSpider(scrapy.Spider):
    name = "sunone"
    allowed_domains = ['wz.sun0769.com']
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest"]

    def parse(self, response):
        item = ItcItem()

        # item['bianhao'] = response.xpath('/html/body/span[1]/text()').extract()[0]
        # item['status'] = response.xpath('/html/body/d2]/text()').extract()
        # item['title'] = response.xpath('/html/body/di/a/text()').extract()
        # item['time'] = response.xpath('/html/body/div[2]/divspan[5]/text()').extract()

        item['bianhao'] = response.css(
            'body > div.public-content > ul.title-state_ul > li:nth-child(1) > span.state1'
        ).extract()[0]
        item['status'] = response.css(
            'body > div.public-content > div.width-12 > ul.title-state-ul > li:nth-child(1) > span.state2'
        ).extract()
        item['title'] = response.css(
            'body > div.public-content > div.width-12 > ul.title-state-ul > li:nth-child(1) > span.state3 > a'
        ).extract()
        item['time'] = response.css(
            'body > div.public-content > div.width-12 > ul.title-state-ul > li:nth-child(1) > span.state5'
        ).extract()

        yield item
