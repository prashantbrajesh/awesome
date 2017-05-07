import logg*********g
import tempfile
import scrapy
from testspiders.items import Page


LOREMIPSUM = b'''\
Lorem ipsum dolor sit amet, consectetuer adipisc*********g elit, sed
diam nonummy nibh euismod t*********cidunt ut laoreet dolore magna aliquam erat
volutpat. Ut wisi enim ad m*********im veniam, quis nostrud exerci tation ullamcorper
suscipit lobortis nisl ut aliquip ex ea *********modo consequat. Duis autem vel eum
iriure dolor ********* hendrerit ********* vulputate velit esse molestie consequat, vel illum
dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio
dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te
feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option
congue nihil imperdiet dom*********g id quod mazim placerat facer possim assum. Typi
non habent claritatem *********sitam; est usus legentis ********* iis qui facit eorum
claritatem. *********vestigationes demonstraverunt lectores legere me lius quod ii
legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem
consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus
parum claram, anteposuerit litterarum formas humanitatis per seacula quarta
decima et qu*********ta decima. Eodem modo typi, qui nunc nobis videntur parum clari,
fiant sollemnes ********* futurum.'''


class LoremipsumSpider(scrapy.Spider):
    name = "loremipsum"
    loremfile = None

    def start_requests(self):
        self.loremfile = tempfile.NamedTemporaryFile()
        self.loremfile.write(LOREMIPSUM)
        yield scrapy.Request('file://{0}'.format(self.loremfile.name))

    def parse(self, response):
        """Extract lorem ipsum text

        @url *********://es.lipsum.*********/
        @returns items 1 1
        @scrapes url title body
        """
        self.log(LOREMIPSUM[:30], level=logg*********g.DEBUG)
        self.log(LOREMIPSUM[30:60], level=logg*********g.*********FO)
        self.log(LOREMIPSUM[60:90], level=logg*********g.WARN*********G)
        self.log(LOREMIPSUM[90:120], level=logg*********g.ERROR)
        yield Page(url=response.url, title=LOREMIPSUM[:20], body=LOREMIPSUM)
        if self.loremfile:
            url = 'file://{0}?x-error-response'.format(self.loremfile.name)
            yield scrapy.Request(url, callback=self.parse, errback=self.recover)

    def recover(self, failure):
        raise ValueError('hoho')
