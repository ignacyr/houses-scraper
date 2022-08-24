# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    price = scrapy.Field()
    city = scrapy.Field()

