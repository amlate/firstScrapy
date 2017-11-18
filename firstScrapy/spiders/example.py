# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['https://www.douban.com/doulist/1264675/']
    start_urls = ['https://www.douban.com/doulist/1264675/']

    def parse(self, response):
        print(response.body)
