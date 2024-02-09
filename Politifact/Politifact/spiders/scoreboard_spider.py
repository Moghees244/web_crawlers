import scrapy
from Politifact.items import ScoreBoard


class ScoreboardSpiderSpider(scrapy.Spider):
    name = "scoreboard_spider"
    allowed_domains = ["www.politifact.com"]
    start_urls = ["https://www.politifact.com/personalities/", "https://www.politifact.com/issues/"]

    custom_settings = {'FEEDS':{'../../scoreboards.csv' : { 'format': 'csv', 'overwrite': 'True'}},}

    def parse(self, response):
        fact_links = response.xpath("//div[@class='c-chyron__value']/a/@href").extract()

        for link in fact_links:
            full_link = "https://www.politifact.com" + link
            yield response.follow(full_link, callback=self.get_scoreboard)
    
    def get_scoreboard(self, response):
        scoreboard = ScoreBoard()

        scoreboard['title'] = response.xpath("//h1[@class='m-pageheader__title']/text()").get()
        stats = response.xpath("//p[@class='m-scorecard__checks']/a/text()").extract()

        if stats:
            scoreboard['true'] = stats[0]
            scoreboard['mostly_true'] = stats[1]
            scoreboard['half_true'] = stats[2]
            scoreboard['mostly_false'] = stats[3]
            scoreboard['false'] = stats[4]
            scoreboard['pants_on_fire'] = stats[5]

        return scoreboard
