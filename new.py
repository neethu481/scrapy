import scrapy
from ..items import ShopsItem


class NewSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['www.carbon38.com']
    start_urls = ['https://www.carbon38.com/product/tessa-top-primary-stripe']

    def parse(self, response):
        items = ShopsItem()

        #breadcrumbs = response.xpath('//*[@id="maincontent"]/div[1]/div[2]/div[1]/ul').get()
        image_url = response.xpath('//*[@id="wrap"]/div').get()
        brand = response.xpath('//*[@id="maincontent"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/a/span').get()
        product_name = response.xpath("//div[@class= 'product_name']/span/text()").get()
        price = response.xpath("//div[@class= 'price-box price-final_price']/span/text()").get()
        reviews = response.xpath('//*[@id="maincontent"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[3]/div').get()
        colour = response.xpath("//span[@class= 'current']/text()").get()
        #size = response.xpath('//*[@id="product-options-wrapper"]/div/div/div/div').get()
        description = response.xpath("//div[@class= 'value']/p/text()").get()
        sku = response.xpath('//*[@id="product.info.sizes"]/div[4]/p').get()


        #items['breadcrumbs'] = breadcrumbs,
        items['image_urls'] = image_url,
        items['brand'] = brand,
        items['product_name'] = product_name,
        items['price'] = price,
        items['reviews'] = reviews,
        items['colour'] = colour,
        #items['size'] = size,
        items['description'] = description,
        items['sku'] = sku,
        yield items
