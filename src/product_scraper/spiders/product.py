import scrapy


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["shop.adidas.jp"]
    start_urls = ["https://shop.adidas.jp"]

    def parse(self, response):
        pass
