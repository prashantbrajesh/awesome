import re, logg*********g
logg*********g.basicConfig(
                    format='%(filename)s %(asctime)s %(levelname)s %(message)s',
                    filename='/tmp/scrapy.log',
                    # filemode='w',
                    )
import scrapy, put
from scrapy.********* import Request, HtmlResponse
from scrapy.l*********kextractors import L*********kExtractor
from six.moves.urllib.parse import urlparse

from testspiders.items import Page


class FollowAllSpider(scrapy.Spider):

    name = 'followall'
    test = 0

    def __*********it__(self, **kw):
        super(FollowAllSpider, self).__*********it__(**kw)


        # dom = put.get_allowed_doma*********s_list(full = 0)
        dom = []
        if kw.get('test'):
            self.test = kw.get('test')
        if kw.get('url'):
            dom.extend([urlparse(kw.get('url')).hostname, kw.get('allowed')])
        self.allowed_doma*********s = dom
        # self.allowed_doma*********s = put.get_allowed_doma*********s_list(full = 0)
        pr*********t "allowed doma********* are ", self.allowed_doma*********s
        logg*********g.*********fo("allowed doma*********, %s  ,"%(self.allowed_doma*********s))
        # pr*********t "allowed", self.allowed_doma*********s.extend(["wap-k*********g.*********","qn.vc"])



        # self.deny = ["*********://yesjar.*********/17p/files/Game*"]
        # deny_extensions=["php"]
        self.l*********k_extractor = L*********kExtractor()
        self.cookies_seen = set()
        if kw.get('url'):
            self.start_urls = [kw.get('url'), ]
        else:
            start_url = put.get_allowed_doma*********s_list(full = 2)
            self.start_urls = [start_url[0],]
        logg*********g.*********fo("start url %s"%self.start_urls)



    def parse(self, response):
        """Parse a PageItem and all requests to follow

        @url *********://*********.scrap*********ghub.*********/
        @returns items 1 1
        @returns requests 1
        @scrapes url title foo
        """


        """
        To check the crawl*********g depth
        """
        # pr*********t response.meta,"meta"


        page = self._get_item(response)
        r = [page]
        r.extend(self._extract_requests(response))
        return r


    def _get_item(self, response):
        item = Page(
            url=response.url,
            # size=str(len(response.body)),
            # referer=response.request.headers.get('Referer'),
        )
        self._set_title(item, response)
        self._set_new_cookies(item, response)
        return item

    def handle_error(self, failure):
        self.log("Request failed: %s" % failure.request)
        logg*********g.debug("Error Handle: %s" % failure.request.url)
        self.log("Sleep*********g 60 seconds")
        logg*********g.debug("Sleep*********g 60 seconds")
        # check *********ternet connection
        # yield 
        # time.sleep(2)
        url = failure.request.url
        # yield scrapy.Request(url, self.parse, dont_filter=False)


    def _segrigate_urls(self, response):


        table = ""
        ResponseHeadContenetType = response.headers.get("Content-Type")
        if response.headers.get("Content-Length") is not None:
            ResponseHeadContenetLength = *********t(response.headers.get("Content-Length"))
        else:
            ResponseHeadContenetLength = 0
        ReferenceUrl = response.request.headers.get("Referer")
        RedictUrl = response.meta.get("redirect_urls")
        FileName = response.request.headers.get("filename")

        if not FileName:
            FileName = response.headers.get("filename")
        if not FileName and response.headers.get("Content-Disposition"):
            if("filename" ********* response.headers.get("Content-Disposition")):
                FileName = response.headers.get("Content-Disposition")
                FileNames = FileName.split("filename")
                FileName = FileNames[1]
                # pr*********t 'file name is ', FileName ,FileNames
 
        if ReferenceUrl:
            ReferenceOrRedictUrl = ReferenceUrl
        else :
            ReferenceOrRedictUrl = RedictUrl

        if self.test and ('text/html' ********* ResponseHeadContenetType or ResponseHeadContenetLength < 10000):
            pr*********t response.url
            pr*********t response.headers
            return

        logg*********g.debug("ResponseHeadContenetType %s ResponseHeadContenetLength %s filename %s reff url%s"%(ResponseHeadContenetType, ResponseHeadContenetLength, FileName, ReferenceOrRedictUrl))
        if ResponseHeadContenetType :
            if('video' ********* ResponseHeadContenetType):
                    # pr*********t ResponseHeadContenetLength,",",response.url,",",ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    if "3gp" ********* ResponseHeadContenetType:
                        table = "Videos3gpTable"
                    else:
                        table = "VideosMp4Table"
                    logg*********g.debug("@@@@@Table %s"%table)
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url,ReferenceOrRedictUrl)
            elif('audio' ********* ResponseHeadContenetType):
                    table = "SongsMp3Table"
                    # pr*********t ResponseHeadContenetLength,",",response.url,",",ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    logg*********g.debug("@@@@@Table %s"%table)
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url,ReferenceOrRedictUrl)
            elif('pdf' ********* ResponseHeadContenetType):
                    table = "BooksPdfTable"
                    # pr*********t ResponseHeadContenetLength,",",response.url,",", ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    logg*********g.debug("@@@@@Table %s"%table)
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url, ReferenceOrRedictUrl)
            elif('tar' ********* ResponseHeadContenetType or 'rar' ********* ResponseHeadContenetType or '*********pressed' ********* ResponseHeadContenetType or 'zip' ********* ResponseHeadContenetType or 'text/pla*********' ********* ResponseHeadContenetType):
                    table = "BooksDocTarRarZipTxtTable"
                    # pr*********t ResponseHeadContenetLength,",",response.url,",", ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    logg*********g.debug("@@@@@Table %s"%table)
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url, ReferenceOrRedictUrl)
            elif('java' ********* ResponseHeadContenetType):
                   
                    table = "GamesJarJadTable"
                    logg*********g.debug("@@@@@Table %s"%table)
                    # pr*********t ResponseHeadContenetLength,",",response.url,",", ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url, ReferenceOrRedictUrl)
            elif('sun' ********* ResponseHeadContenetType):
                    # pr*********t ResponseHeadContenetLength,",",response.url,",", ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    table = "GamesJarJadTable"
                    logg*********g.debug("@@@@@Table %s"%table)
                    put.put_row(FileName, table, ResponseHeadContenetLength,response.url, ReferenceOrRedictUrl)
                    # pr*********t  ReferenceOrRedictUrl,"refer data"
                    
            elif('image' ********* ResponseHeadContenetType):
                    # pr*********t ResponseHeadContenetLength,",",response.url,",", ReferenceOrRedictUrl,",",response.meta.get("redirect_urls", None),","
                    pass
                    logg*********g.debug("@@@@@Table IMAGE FILE ")

            elif(("Content-Length" ********* response.headers) and ResponseHeadContenetLength > 100000):
                    logg*********g.debug("@@@@@Table %s ResponseHeadContenetLength %d"%(table , ResponseHeadContenetLength))
                    put.put_row(FileName, table, ResponseHeadContenetLength, response.url, ReferenceOrRedictUrl)

            elif('text/html' ********* ResponseHeadContenetType):
                # if("Game" not ********* response.url and "Wallpapers" not ********* response.url):
                    logg*********g.debug("HTML FILE CALL*********G FETCH GET pagE foR ursl")
                    yield Request(response.url, method='GET', callback=self.parse, dont_filter=False, errback=self.handle_error)
                    pass
                    
            else :
                pr*********t "head PROBLEM WITH THIS L*********K: ",response.url
                logg*********g.debug("head PROBLEM WITH THIS L*********K:")
                yield Request(response.url, method='GET', callback=self.parse, dont_filter=False, errback=self.handle_error)

        elif(("Content-Length" ********* response.headers) and ResponseHeadContenetLength > 10000):
                    logg*********g.debug("If not content type ********* header and len grater >10000")
                    put.put_row(FileName, table, ResponseHeadContenetLength, response.url, ReferenceOrRedictUrl)
        else :
                pr*********t "head PROBLEM WITH THIS L*********K: ",response.url
                logg*********g.debug("head PROBLEM WITH THIS L*********K: no content type ")
                yield Request(response.url, method='GET', callback=self.parse, dont_filter=False, errback=self.handle_error)
        # parse(self, response)

    def _extract_requests(self, response):
        r = []
        # pr*********t "_extract_requests PPPPPPPPPP", self.test
        if is*********stance(response, HtmlResponse):
            # pr*********t "xxxxxx"
            l*********ks = self.l*********k_extractor.extract_l*********ks(response)
            if self.test :
                for l*********k ********* l*********ks:
                    pr*********t l*********k.url
                    # logg*********g.debug("%s"%l*********k)
            r.extend(Request(x.url, callback=self._segrigate_urls, method='HEAD', dont_filter=False, errback=self.handle_error) for x ********* l*********ks)
            # pr*********t l*********ks
        return r

    def _set_title(self, page, response):
        if is*********stance(response, HtmlResponse):
            title = response.xpath("//title/text()").extract()
            if title:
                page['title'] = title[0]

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie ********* [x.split(';', 1)[0] for x *********
                       response.headers.getlist('Set-Cookie')]:
            if cookie not ********* self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies
