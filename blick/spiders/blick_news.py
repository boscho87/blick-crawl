import json
from datetime import datetime
import scrapy, time
import re


class BlickNews(scrapy.Spider):
    name = 'blick'
    comment_base_url = 'https://community.ws.blick.ch/community/comment?page=0&discussion_type_id='
    start_urls = [
        'https://www.blick.ch/services/webarchiv/'
    ]

    def parse(self, response):
        for link in response.css('div.flexitem a.clickable::attr("href")'):
            yield response.follow(link.get(), callback=self.parse_post)

    def parse_post(self, response):
        try:
            response.url.index('webarchiv')
            return
        except:
            id = re.search('id(\d+)', response.url).group(1)  # extract id from id1234345
            comment_url = self.comment_base_url + id
            yield {
                'id': id,
                'date': datetime.now(),
                'timestamp': time.time(),
                'url': response.url,
                'title': response.css("title::text").get(),
                'teaser': response.css(".article-lead::text").get(),
                'author': response.css(".flexitem .pianocontainer + div span::text").get(),
                'publish_date': response.css(".article-metadata > div > div::text").get(),
                'update_date': response.css(".article-metadata > div > div + div + div ::text").get(),
                'body': response.css(".article-body").getall(),
                # 'comments_count': response.css(".comment-button::text").get()
                'comments': scrapy.Request(comment_url, callback=self.get_comments) # todo check, why the URL is in the json, not the yield content
            }

    def get_comments(self, response):
        yield json.loads(response.body)
