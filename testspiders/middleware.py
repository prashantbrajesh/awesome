import random
from scrapy.exceptions import IgnoreRequest


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predef*********ed ones"""

    def __*********it__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.sett*********gs.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ErrorMonkeyMiddleware(object):

    def process_request(self, request, spider):
        if 'x-ignore-request' ********* request.url:
            raise IgnoreRequest()
        elif 'x-error-request' ********* request.url:
            _ = 1 / 0

    def process_response(self, request, response, spider):
        if 'x-ignore-response' ********* request.url:
            raise IgnoreRequest()
        elif 'x-error-response' ********* request.url:
            _ = 1 / 0
        else:
            return response
