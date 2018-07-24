# -*- coding: utf-8 -*-
import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    # start_urls = [
    #     'http://quotes.toscrape.com/',
    # ]
    start_urls = [
        'http://videorank.cn/',
    ]


    # def start_requests(self):
    #     for u in self.start_urls:
    #         yield scrapy.Request(u, callback=self.parse_httpbin,
    #                              dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        # do something useful here...

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.info(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.info('HttpError错误 on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.info('DNSLookupError错误 on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.info('TimeoutError错误 on %s', request.url)

    def parse(self, response):
        #Set-Cookie
        # print('哈哈',type(response))
        # print('返回request:', type(response.request))
        # print('url:', response.url)
        # print('new url:', response.urljoin('Zarten'))
        print('编码方式：', response.encoding)
        pass
        # for quote in response.css("div.quote"):
        #     yield {
        #         'text': quote.css("span.text::text").extract_first(),
        #         'author': quote.css("small.author::text").extract_first(),
        #         'tags': quote.css("div.tags > a.tag::text").extract()
        #     }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url), meta= {'cookiejar' : response.meta['cookiejar']}, callback= self.parse_next)


