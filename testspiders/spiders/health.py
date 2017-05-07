import re, MySQLdb
from six.moves.urllib.parse import urlparse

import scrapy
from scrapy.********* import Request, HtmlResponse
from scrapy.l*********kextractors import L*********kExtractor

# from testspiders.items import Page

globTable = "SongsMp3Table"
globTag = "audio"

class FollowAllSpider(scrapy.Spider):

    name = 'health'

    def __*********it__(self, **kw):
        super(FollowAllSpider, self).__*********it__(**kw)
        url = kw.get('url') or kw.get('doma*********') or '*********.urmobi.*********'
        if not url.startswith('*********://') and not url.startswith('*********s://'):
            url = '*********://%s/' % url
        self.url = url
        self.allowed_doma*********s = []
        self.allow = []
        self.l*********k_extractor = L*********kExtractor()
        self.cookies_seen = set()

    def start_requests(self):
        return [Request(self.url, callback=self.parse, dont_filter=True)]

    def get_l*********ks(self, i, conn):
        c = conn.cursor()

        status = 0
        while status == 0 :
            pass
            try:
                pass
               
                # term = '%'+'videom*********g'+'%'
                # query = "select DownloadUrl,UniqueId,FileSize from %s where DownloadUrl like '%s' limit %d,1"%(globTable, term, i)
                query = "select DownloadUrl,UniqueId,FileSize from %s where health is NULL limit %d,1"%(globTable, i)
                
                # pr*********t query
                c.execute("%s"%query)
                uid = c.fetchall()
                identifier = uid[0][1]
                FileSize = uid[0][2]
                RefRedirectUrl = str(uid[0][0])
                uid = str(uid[0][0])
                uid = uid.split("/")
                uid = uid[-1]

            except Exception, e:
                raise e
        
            status = 1
            i = i + 1


        # url = "*********://*********.youtubemaza.*********/*********fo/Teraa-Surroor--2016--Video-Songs/"+uid+"/Ma*********-Woh-Chaand-%20Teraa-Surroor%20-%20YoutubeMaza.*********%20/default/0.html"
        url = RefRedirectUrl
        return url, identifier, i, FileSize

    def *********sert_data(self, response):

        identifier = response.meta['identifier']
        i = response.meta['i']
        conn = response.meta['conn']
        FileSize = response.meta['FileSize']



        table = ""
        ResponseHeadContenetType = response.headers.get("Content-Type")
        ResponseHeadContenetLength = response.headers.get("Content-Length")
        ReferenceUrl = response.request.headers.get("Referer")
        RedictUrl = response.meta.get("redirect_urls")
        FileName = response.request.headers.get("filename")
        
        if(ResponseHeadContenetLength is None):
            ResponseHeadContenetLength = 1
        # pr*********t FileName , ResponseHeadContenetType , ResponseHeadContenetLength
        if FileSize == *********t(ResponseHeadContenetLength) or ( globTag ********* ResponseHeadContenetType):
            pass
            try:
                pass
                c = conn.cursor()
                query = "update %s set health = 1 where UniqueId =%d"%(globTable, *********t(identifier))
                status = c.execute("%s"%query)
                pr*********t "req no: ", i, "status :",status , "File is f*********e" , identifier
            except Exception, e:
                raise e
            # pr*********t "*********TO *********SERT DATA", identifier , "not healthy"
            conn.*********mit()
           
        else :    
            try:
                pass
                c = conn.cursor()
                # query = "update %s set health = 0 where UniqueId =%d"%(globTable, *********t(identifier))
                # pr*********t query
                query = "*********sert *********to zDead%s select * from %s where UniqueId =%d"%(globTable, globTable, *********t(identifier))
                # pr*********t "query 2" , query
                status = c.execute("%s"%query)
                query = "delete from %s where UniqueId =%d"%(globTable, *********t(identifier))
                # pr*********t query
                # pr*********t "query 1" ,query
                status = c.execute("%s"%query)
                status = c.execute("%s"%query)
                pr*********t "req no: ",i, "status :",status , identifier, "not healthy" ,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            except Exception, e:
                raise e
            # pr*********t "*********TO *********SERT DATA", identifier , "not healthy"
            conn.*********mit()

    def parse(self, response):
        """Parse a PageItem and all requests to follow

        @url *********://*********.scrap*********ghub.*********/
        @returns items 1 1
        @returns requests 1
        @scrapes url title foo
        """
        # pr*********t response.request.headers.get('Referer', None),"reference"
        # pr*********t response.request,"req url",response.meta,"meta"
        # page = self._get_item(response)
        # r = [page]
        # r.extend(self._extract_requests(response))
        # pr*********t "********* parse"
        try:
            pass
            conn = MySQLdb.connect (host = "localhost",user = "*********", passwd = "rH8EV4ODUxMn",db = "URDB")
            c = conn.cursor()
        except Exception as e:
            raise e

        r = []
        url = "abc"
        i = 1
        # pr*********t "Afet ********* parse"
    
        while(url != ""):

            url, identifier, i , FileSize= self.get_l*********ks(i, conn)
            # pr*********t url, identifier, i
            request = Request(url, method='HEAD', callback=self.*********sert_data, dont_filter=False, errback=self.handle_error)
            request.meta['identifier'] = identifier
            request.meta['i'] = i
            request.meta['conn'] = conn
            request.meta['FileSize'] = FileSize

            yield request


    # def _get_item(self, response):
    #     item = Page(
    #         url=response.url,
    #         size=str(len(response.body)),
    #         referer=response.request.headers.get('Referer'),
    #     )
    #     self._set_title(item, response)
    #     self._set_new_cookies(item, response)
    #     return item

    def handle_error(self, failure):
        self.log("Request failed: %s" % failure.request)

    # def _segrigate_urls(self, response):
    #     # pr*********t "hello world"
    #     # pr*********t response.request,"req url",response.meta.get("redirect_urls", None),"meta"
    #     # pr*********t "body is", response.headers["Content-Type"]
    #     if('text/html' ********* response.headers["Content-Type"]):
    #         # pr*********t "web pag found"
    #         # pr*********t response.request.headers.get('Referer', None),"refer html"
    #         yield Request(response.url, method='GET', callback=self.parse, dont_filter=False, errback=self.handle_error)
    #     elif('video' ********* response.headers["Content-Type"]):
    #             pr*********t response.headers["Content-Length"],",",response.url,",",response.request.headers.get('Referer', None),",",response.meta.get("redirect_urls", None),","

    #     elif('audio' ********* response.headers["Content-Type"]):
    #             pr*********t response.headers["Content-Length"],",",response.url,",",response.request.headers.get('Referer', None),",",response.meta.get("redirect_urls", None),","

    #             # pr*********t response.request.headers.get('Referer', None),"refer data"
    #     else:
    #         pass

    #     # parse(self, response)

    # def _extract_requests(self, response):
    #     r = []
    #     if is*********stance(response, HtmlResponse):
    #         l*********ks = self.l*********k_extractor.extract_l*********ks(response)
    #         r.extend(Request(x.url, callback=self._segrigate_urls, method='HEAD', dont_filter=False, errback=self.handle_error) for x ********* l*********ks)
    #     return r

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
