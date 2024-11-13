import os

import scrapy

from ..items import ZameenhomeItem

class QuotesSpider(scrapy.Spider):
    name = "homes"
    start_urls = [
        "https://www.zameen.com/Homes/Lahore-1-1.html",
    ]



    def parse(self, response):
        for home in response.css("li.a37d52f0"):
            data = ZameenhomeItem()
            home_link = home.css("a::attr(href)").get()
            data['home_url'] = response.urljoin(home_link)
            data['deal_type'] = home.css("div._021a5aeb::text").extract()

            is_titanium = home.css("span.b86424a1::text").get()
            data['is_titanium'] = self.checkbadge("Titanium", is_titanium)

            is_trusted = home.css('svg._552d4639::attr(aria-label)').get()
            data['is_trusted'] = self.checkbadge("Trusted badge", is_trusted)

            is_verified = home.css('svg._70461b5f::attr(aria-label)').get()
            data['is_verified'] = self.checkbadge("Verified badge", is_verified)

            yield response.follow(data['home_url'], self.parse_home_details, meta={'data': data})

            next_page = response.css("a._95dd93c1[title='Next']::attr(href)").get()
            if next_page:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_home_details(self, response):
        data = response.meta['data']
        details = {}

        details['address'] = response.css('div.cd230541::text').get()
        details['title'] = response.css("h1.aea614fd::text").get()
        details['currency'] = response.css("span.aa458c2e::text").get()
        details['house_type'] = response.css("span._2fdf7fc5::text").get()
        details['price'] = response.css("span._63ea997b::text").get()
        details['price_in_rupees'] = self.convert_price_to_number(details['price'])

        details['area'] = response.css("li span[aria-label='Area'] span::text").get()
        details['purpose'] = response.css("li span[aria-label='Purpose']::text").get()
        details['location'] = response.css("li span[aria-label='Location']::text").get()
        details['bedrooms'] = response.css("li span[aria-label='Beds']::text").get()
        details['bath'] = response.css("li span[aria-label='Baths']::text").get()
        details['added'] = response.css("li span[aria-label='Creation date']::text").get()

        description_container = response.css("div._1e8e64c5")
        details['description'] = description_container.css("span._3547dac9::text").getall()

        amenities = {}
        for amenity in response.css("li._51519f00"):
            feature_name = amenity.css('div.d0142259::text').get()
            values = []
            for feature_values in amenity.css("li._59261156"):
                value = feature_values.css('span._9121cbf9::text').getall()
                values.append(''.join(value))
            amenities[feature_name] = values

        item = ZameenhomeItem(**{**data, **details, 'amenities': amenities})
        yield item

    def convert_price_to_number(self, price):
        if price:
            price = price.replace(',', '').strip()
            if 'Crore' in price:
                value = float(price.replace('Crore', '').strip())
                return value * 10000000
            elif 'Lakh' in price:
                value = float(price.replace('Lakh', '').strip())
                return value * 100000
            elif 'Arab' in price:
                value = float(price.replace('Arab', '').strip())
                return value * 1000000000
            else:
                return float(price.replace('0', '').strip().replace(',', ''))
        return None

    def checkbadge(self, badgeName, value):
        if badgeName == value:
            return "yes"
        else:
            return "no"
