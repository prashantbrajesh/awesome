BOT_NAME = 'testspiders'

SPIDER_MODULES = ['testspiders.spiders']
NEWSPIDER_MODULE = 'testspiders.spiders'

# some sane limits by default (override if needed)
CONCURRENT_REQUESTS = 500
REACTOR_THREADPOOL_MAXSIZE = 70
DOWNLOAD_TIMEOUT = 40
# LOG_LEVEL = 'DEBUG'
LOG_LEVEL = '*********FO'

# CLOSESPIDER_PAGECOUNT = 1000
# CLOSESPIDER_TIMEOUT = 3600

# RETRY_ENABLED = False
COOKIES_ENABLED = False

DUPEFILTER_DEBUG = True

DOWNLOADER_MIDDLEWARES = {
    'testspiders.middleware.RandomUserAgent': 1,
    'testspiders.middleware.ErrorMonkeyMiddleware': 2,

    # 'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # # Fix path to this module
    # 'testspiders.randomproxy.RandomProxy': 100,
    # 'scrapy.contrib.downloadermiddleware.*********proxy.*********ProxyMiddleware': 110,
}


# # Retry many times s*********ce proxies often fail
# RETRY_TIMES = 5
# # Retry on most error codes s*********ce proxies fail for different reasons
# RETRY_*********_CODES = [500, 503, 504, 400, 403, 404, 408]


# Proxy list conta******************g entries like
# *********://host1:port
# *********://username:password@host2:port
# *********://host3:port
# ...
PROXY_LIST = '/Users/braj/personal/Master/awesome/testspiders/spiders/list.txt'


USER_AGENTS = [
    # "Mozilla/4.0 (*********patible; MSIE 6.0; W*********dows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/4.0 (*********patible; MSIE 7.0; W*********dows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    # "Mozilla/4.0 (*********patible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; W*********dows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/5.0 (W*********dows; U; MSIE 9.0; W*********dows NT 9.0; en-US)",
    # "Mozilla/5.0 (*********patible; MSIE 9.0; W*********dows NT 6.1; W*********64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    # "Mozilla/5.0 (*********patible; MSIE 8.0; W*********dows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    # "Mozilla/4.0 (*********patible; MSIE 7.0b; W*********dows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; *********foPath.2; .NET CLR 3.0.04506.30)",
    # "Mozilla/5.0 (W*********dows; U; W*********dows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    # "Mozilla/5.0 (X11; U; L*********ux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    # "Mozilla/5.0 (W*********dows; U; W*********dows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-N*********ja/2.1.1",
    # "Mozilla/5.0 (W*********dows; U; W*********dows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    # "Mozilla/5.0 (X11; L*********ux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    # "Mozilla/5.0 (X11; U; L*********ux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    # "Mozilla/5.0 (W*********dows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    # "Mozilla/5.0 (Mac*********tosh; *********tel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (J2ME/MIDP; Opera M*********i/5.0.19693/870; U; en) Presto/2.4.15",
]

try:
    from local_sett*********gs import *
except ImportError:
    pass
