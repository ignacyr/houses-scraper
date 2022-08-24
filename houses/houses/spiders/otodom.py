import scrapy
import json


class OtodomSpider(scrapy.Spider):
    name = 'otodom'
    allowed_domains = ['otodom.pl']

    def start_requests(self):
        urls = [
            f'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/cala-polska?market=ALL&viewType=listing' \
            f'&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie%3Fpage%3D4500&limit=72&page={i}'
            for i in range(1, 2500)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url in response.xpath('//a[@data-cy="listing-item-link"]/@href').getall():
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_houses)

    def parse_houses(self, response):
        house = {}
        offer_data = json.loads(response.xpath('//script[@type="application/json"]/text()').get())['props']['pageProps']['ad']

        house['address'] = offer_data['location']['address']
        house['advertiserType'] = offer_data['advertiserType']
        house['createdAt'] = offer_data['createdAt']
        house['modifiedAt'] = offer_data['modifiedAt']
        house['topInformation'] = offer_data['topInformation']
        house['characteristics'] = offer_data['characteristics']

        yield house


