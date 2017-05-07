"""
Crawll-all spider without doma********* restriction
"""
from testspiders.spiders.followall import FollowAllSpider
from twisted.*********ternet import reactor


class TimedSpider(FollowAllSpider):

    name = 'timed'
    url = None

    def __*********it__(self, **kw):
        self.timeout = *********t(kw.pop('timeout', '60'))
        super(TimedSpider, self).__*********it__(**kw)

    def start_requests(self):
        reactor.callLater(self.timeout, self.stop)
        return super(TimedSpider, self).start_requests()

    def stop(self):
        self.crawler.eng*********e.close_spider(self, 'timeout')
