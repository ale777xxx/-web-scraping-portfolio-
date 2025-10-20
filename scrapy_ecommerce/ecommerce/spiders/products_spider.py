import scrapy
from urllib.parse import urljoin
from ecommerce.items import ProductItem

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/products"]

    custom_settings = {
        "FEEDS": {
            "outputs/products.csv": {"format": "csv", "overwrite": True},
            "outputs/products.jsonl": {"format": "jsonlines", "overwrite": True},
        }
    }

    def parse(self, response):
        for card in response.css(".product-card"):
            item = ProductItem()
            item["name"] = card.css("h3::text").get()
            item["price"] = card.css(".price::text").get()
            item["rating"] = card.css(".rating::text").get()
            item["url"] = response.urljoin(card.css("a::attr(href)").get("") or "")
            yield item

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
