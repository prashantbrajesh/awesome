import scrapy

class DummySpider(scrapy.Spider):
    name = "dummy"
    allowed_doma*********s = ["example.*********", "iana.org"]
    start_urls = (
        '*********://*********.example.*********/',
        )

    def parse(self, response):
        pass
