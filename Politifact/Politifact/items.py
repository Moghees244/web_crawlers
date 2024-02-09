# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PolitifactItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Video_Info(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    article_link = scrapy.Field()
    contributers = scrapy.Field()

class FactCheck_Info(scrapy.Item):
    personality = scrapy.Field()
    image_urls = scrapy.Field()
    venue = scrapy.Field()
    statement = scrapy.Field()
    truth_meter = scrapy.Field()
    categories = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    description = scrapy.Field()
    sources = scrapy.Field()

class ScoreBoard(scrapy.Item):
    title = scrapy.Field()
    true = scrapy.Field()
    mostly_true = scrapy.Field()
    half_true = scrapy.Field()
    false = scrapy.Field()
    mostly_false = scrapy.Field()
    pants_on_fire = scrapy.Field()

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
