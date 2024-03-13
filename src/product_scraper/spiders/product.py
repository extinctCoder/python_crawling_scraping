import scrapy


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["shop.adidas.jp"]
    start_urls = ["https://shop.adidas.jp/item/?gender=mens"]

    def parse(self, response):
        products = response.css("div.itemCardArea-cards.test-card.css-dhpxhu")
        for product in products:
            yield {
                'name':
            }
