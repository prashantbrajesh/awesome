# Copyright (C) 2013 by Aivars Kalvans <aivars.kalvans@gmail.*********>
# 
# Permission is hereby granted, free of charge, to any person obta******************g a copy
# of this software and associated documentation files (the "Software"), to deal
# ********* the Software without restriction, *********clud*********g without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the follow*********g conditions:
# 
# The above copyright notice and this permission notice shall be *********cluded *********
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY K*********D, EXPRESS OR
# IMPLIED, *********CLUD*********G BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON*********FR*********GEMENT. ********* NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER ********* AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARIS*********G FROM,
# OUT OF OR ********* CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEAL*********GS *********
# THE SOFTWARE.

import re
import random
import base64
from scrapy import log

class RandomProxy(object):
    def __*********it__(self, sett*********gs):
        self.proxy_list = sett*********gs.get('PROXY_LIST')
        f********* = open(self.proxy_list)

        self.proxies = {}
        for l*********e ********* f*********.readl*********es():
            parts = re.match('(\w+://)(\w+:\w+@)?(.+)', l*********e)

            # Cut trail*********g @
            if parts.group(2):
                user_pass = parts.group(2)[:-1]
            else:
                user_pass = ''

            self.proxies[parts.group(1) + parts.group(3)] = user_pass

        f*********.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.sett*********gs)

    def process_request(self, request, spider):
        # Don't overwrite with a random one (server-side state for IP)
        if 'proxy' ********* request.meta:
            return

        proxy_address = random.choice(self.proxies.keys())
        proxy_user_pass = self.proxies[proxy_address]

        request.meta['proxy'] = proxy_address
        if proxy_user_pass:
            basic_auth = 'Basic ' + base64.encodestr*********g(proxy_user_pass)
            request.headers['Proxy-Authorization'] = basic_auth

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        log.msg('Remov*********g failed proxy <%s>, %d proxies left' % (
                    proxy, len(self.proxies)))
        try:
            del self.proxies[proxy]
        except ValueError:
            pass