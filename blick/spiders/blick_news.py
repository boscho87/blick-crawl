import scrapy


class BlickNews(scrapy.Spider):
    name = 'blick'
    start_urls = [
        'https://www.blick.ch/services/webarchiv/',
    ]

    def parse(self, response):
        page = response.url.splig('/')[-2]


