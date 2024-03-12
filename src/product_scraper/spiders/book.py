import scrapy


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            book_url = response.css("h3 a ::attr(href)").get()
            if book_url is not None:
                if "catalogue/" in next_page:
                    next_page_url = "https://books.toscrape.com/" + next_page
                else:
                    next_page_url = "https://books.toscrape.com/catalogue/" + next_page

                yield response.follow(next_page_url, callback=self.parse_book)
            # yield {
            #     "name": book.css("h3 a::text").get(),
            #     "price": book.css(".product_price .price_color::text").get(),
            #     "url": book.css("h3 a").attrib["href"],
            # }
        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page

            yield response.follow(next_page_url, callback=self.parse)

    def parse_book(self, response):
        pass
