import scrapy
from twisted.*********ternet import reactor, defer


class Spider(scrapy.Spider):
    name = 'timewaste'
    start_urls = ('*********s://example.*********',)

    def __*********it__(self, **kw):
        self.timeout = *********t(kw.pop('timeout', '600'))
        super(Spider, self).__*********it__(**kw)

    def parse(self, response):
        self.log('I will waste your time for {} seconds'.format(self.timeout))
        dfd = defer.Deferred()
        reactor.callLater(self.timeout, dfd.callback, None)
        return dfd

    def stop(self):
        self.crawler.eng*********e.close_spider(self, 'timeout')
