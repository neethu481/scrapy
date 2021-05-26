import scrapy
from ..items import ShopItem


class WearSpider(scrapy.Spider):
    name = 'wear'
    allowed_domains = ['www.carbon38.com']
    start_urls = ['https://www.carbon38.com/shop-all-activewear/tops']

    page_number = 2

    def parse(self, response):
        items = ShopItem()
        brands = response.css('.brand a::text').extract()
        item_link = response.css('.product-item-link::attr(href)').extract()
        price = response.css('.price::text').extract()
        image_urls = response.css('.product-image-photo::attr(src)').extract()
        best_seller = response.css('.in-stock-state-bestsellers_cat::text').extract()
        matching_price = response.css('.label::text').extract()
        exclusive = response.css('.catalog_exclusive::text').extract()

        items['brands'] = brands
        items['item_link'] = item_link
        items['price'] = price
        items['image_urls'] = image_urls
        items['best_seller'] = best_seller
        items['matching_price'] = matching_price
        items['exclusive'] = exclusive

        yield items

        next_page = 'https://www.carbon38.com/shop-all-activewear/tops?p=' + str(WearSpider.page_number) + '&dir=&order=&limit=60'
        if WearSpider.page_number <= 10:
            WearSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
