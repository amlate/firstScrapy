import scrapy
import re

class dbbookSpider(scrapy.Spider):
    name = "dbbook"
    start_urls = ["https://www.douban.com/doulist/1264675/"]

    def parse(self, response):
        selector = scrapy.Selector(response)
        books=selector.xpath('//div[@class="bd doulist-subject"]')
        for book in books:
            try:
                title = book.xpath('div[@class="title"]/a/text()').extract()[0].replace(' ','').replace('\n','')
                rate = book.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
                author = re.search('div class="abstract">(.*?)<br',book.extract(),re.S).group(1).replace(' ','').replace('\n','')
                print("标题：",title)
                print("评分：", rate)
                print("作者：", author)
            except BaseException:
                pass

        nextPage=selector.xpath('//span[@class="next"]/link/@href').extract()
        print(nextPage)
        if nextPage:
            next=nextPage[0]
            yield  scrapy.http.Request(next,callback=self.parse)

