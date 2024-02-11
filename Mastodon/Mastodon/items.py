# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MastodonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Media_Attachment(scrapy.Item):
    media_type = scrapy.Field()
    image_urls = scrapy.Field()
    description = scrapy.Field()

class Post_Info(scrapy.Item):
    id = scrapy.Field()
    username = scrapy.Field()
    created_at = scrapy.Field()
    sensitive = scrapy.Field()
    language = scrapy.Field()
    url = scrapy.Field()
    replies_count = scrapy.Field()
    reblogs_count = scrapy.Field()
    favourites_count = scrapy.Field()
    content = scrapy.Field()
    mentions = scrapy.Field()
    tags = scrapy.Field()
    card = scrapy.Field()
    poll = scrapy.Field()
    media = scrapy.Field()
    image_urls = scrapy.Field()

class Account_Info(scrapy.Item):
    username = scrapy.Field()
    display_name = scrapy.Field()
    note = scrapy.Field()
    url = scrapy.Field()
    avatar = scrapy.Field()
    followers_count = scrapy.Field()
    following_count = scrapy.Field()
    statuses_count = scrapy.Field()
    fields = scrapy.Field()