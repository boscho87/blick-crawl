import json
from datetime import datetime
import scrapy, time
import re


class BlickNews(scrapy.Spider):
    name = 'blick'
    comment_base_url = 'https://community.ws.blick.ch/community/comment?page={}&discussion_type_id={}'
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
            post_id = re.search('id(\d+)', response.url).group(1)
            comment_url = self.comment_base_url.format(0, post_id)
            data = {
                'post_id': post_id,
                'date': datetime.now(),
                'timestamp': time.time(),
                'url': response.url,
                'title': response.css("title::text").get(),
                'teaser': response.css(".article-lead::text").get(),
                'author': response.css(".flexitem .pianocontainer + div span::text").get(),
                'publish_date': response.css(".article-metadata > div > div::text").get(),
                'update_date': response.css(".article-metadata > div > div + div + div ::text").get(),
                'body': response.css(".article-body").getall(),
                'comments': [],
            }
            yield scrapy.Request(comment_url, callback=self.get_comments, cb_kwargs=data)

    def get_comments(self, response, **data):
        comments = json.loads(response.body)
        is_last_page = comments['last']
        comment_page_number = comments['number']
        comment_list = data['comments']

        next_page_url = self.comment_base_url.format(comment_page_number + 1, data['post_id'])

        for comment_data in comments['content']:
            comment = self.extract_comment_data(comment_data, True)
            comment['current_page'] = response.url
            comment['next_page'] = next_page_url
            comment['has_next'] = not is_last_page
            comment_list.append(comment)

        data['comments'] = comment_list

        if is_last_page:
            yield data

        yield scrapy.Request(next_page_url, callback=self.get_comments, cb_kwargs=data)

    def extract_comment_data(self, comment_data, go_deeper=False):
        data = {
            'created': comment_data['created'],
            'modified': comment_data['modified'],
            'body': comment_data['body'],
            'user': comment_data['user']['name'],
            'reaction_like': comment_data['reaction1_count'],
            'reaction_disagree': comment_data['reaction2_count'],
            'user_enabled': comment_data['user']['status_id'],
            'user_id': comment_data['user']['user_id'],
            'comment_id': comment_data['id'],
        }
        if go_deeper:
            data['answers'] = self.extract_answers(comment_data['answers']),

        return data

    def extract_answers(self, answers):
        formatted_answers = []
        for answer in answers:
            formatted_answers.append(self.extract_comment_data(answer))

        return formatted_answers
