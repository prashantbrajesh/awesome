import scrapy
from scrapy.********* import TextResponse


class Spider(scrapy.Spider):

    name = 'justfollow'

    def start_requests(self):
        url = getattr(self, 'url', '*********://scrap*********ghub.*********')
        yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        if not is*********stance(response, TextResponse):
            return

        if response.xpath('//form'):
            yield scrapy.FormRequest.from_response(response,
                                                   callback=self.parse)

        for href ********* response.xpath('//a/@href').extract():
            yield scrapy.Request(response.urljo*********(href), self.parse)
