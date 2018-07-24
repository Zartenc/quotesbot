# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ToScrapeSpiderXPath(CrawlSpider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    #第一个Rule包含了第二个Rule，不会执行第二个Rule
    #follow会一直循环嵌套的爬完所有的链接，直到没有链接可爬
    rules = (
        Rule(link_extractor= LinkExtractor(deny=('page/2')), callback= 'parse_item_first', follow= True),
        Rule(link_extractor=LinkExtractor(allow=('page/3')), callback= 'parse_item_second')

    )

    def parse_item_first(self, response):
        print('parse_item_first:', response.url)

    def parse_item_second(self, response):
        print('parse_item_second:', response.url)

    def parse_start_url(self, response):
        print('parse_start_url:', response.url)
        # for quote in response.xpath('//div[@class="quote"]'):
        #     yield {
        #         'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
        #         'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
        #         'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        #     }
        #
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

