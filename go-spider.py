from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from blick.spiders.blick_news import BlickNews

process = CrawlerProcess(get_project_settings())
process.crawl(BlickNews)
process.start()
