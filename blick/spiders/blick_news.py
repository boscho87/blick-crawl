from datetime import datetime
import scrapy, time
from scrapy_splash import  SplashRequest


class BlickNews(scrapy.Spider):
    name = 'blick'

    def start_requests(self):
        yield SplashRequest(
            url='https://www.blick.ch/services/webarchiv/',
            callback=self.parse
        )

    def parse(self, response):
        for link in response.css('div.flexitem a.clickable::attr("href")'):
            yield response.follow(link.get(), callback=self.parse_post)

    def parse_post(self, response):
        try:
            response.url.index('webarchiv')
            return
        except:
            yield {
                'date': datetime.now(),
                'timestamp': time.time(),
                'url': response.url,
                'title': response.css("title::text").get(),
                'teaser': response.css(".article-lead::text").get(),
                'author': response.css(".flexitem .pianocontainer + div span::text").get(),
                'publish_date': response.css(".article-metadata > div > div::text").get(),
                'update_date': response.css(".article-metadata > div > div + div + div ::text").get(),
                'body': response.css(".article-body").getall(),
                'comments_count': response.css(".comment-button::text").get()
            }
