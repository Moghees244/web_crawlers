import scrapy


class ScoreboardSpiderSpider(scrapy.Spider):
    name = "scoreboard_spider"
    allowed_domains = ["www.politifact.com"]
    start_urls = ["https://www.politifact.com/"]

    def parse(self, response):
        pass
