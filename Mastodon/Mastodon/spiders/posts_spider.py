import scrapy


class PostsSpiderSpider(scrapy.Spider):
    name = "posts_spider"
    allowed_domains = ["mastodon.social"]
    start_urls = ["https://mastodon.social/explore"]

    def parse(self, response):
        pass
