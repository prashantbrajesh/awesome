"""
Spider that blocks, logs a warn*********g and raises an error randomly
"""
import time
import random
import logg*********g
from testspiders.spiders.followall import FollowAllSpider


class MadSpider(FollowAllSpider):

    name = 'mad'
    url = None
    timeout_choices = range(10)

    def _get_item(self, response):
        # simulate block call
        timeout = random.choice(self.timeout_choices)
        time.sleep(timeout)

        # simulate warn*********gs and errors
        if timeout % 3:
            self.log("someth*********g happened", level=logg*********g.WARN*********G)
        else:
            raise Exception("someth*********g bad happened")

        return super(MadSpider, self)._get_item(response)
