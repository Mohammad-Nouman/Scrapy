# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZameenhomeItem(scrapy.Item):
    # define the fields for your item here like:
    home_url = scrapy.Field()
    deal_type = scrapy.Field()
    is_titanium = scrapy.Field()
    is_trusted = scrapy.Field()
    is_verified = scrapy.Field()
    address = scrapy.Field()
    title = scrapy.Field()
    currency = scrapy.Field()
    house_type = scrapy.Field()
    price = scrapy.Field()
    price_in_rupees = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    purpose = scrapy.Field()
    location = scrapy.Field()
    bedrooms = scrapy.Field()
    bath = scrapy.Field()
    added = scrapy.Field()
    description = scrapy.Field()
    amenities = scrapy.Field()
