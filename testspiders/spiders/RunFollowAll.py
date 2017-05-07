from scrapy.crawler import CrawlerProcess
from followall import FollowAllSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (*********patible; MSIE 7.0; W*********dows NT 5.1)'
})

FollowAllSpider.test = 1


process.crawl(FollowAllSpider, allowed_doma*********s='scrap*********ghub.*********')
process.start() # the script will block here until the crawl*********g is f*********ished