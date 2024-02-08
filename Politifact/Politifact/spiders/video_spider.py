import scrapy
from Politifact.items import Video_Info


class VideoSpiderSpider(scrapy.Spider):
    name = "video_spider"
    allowed_domains = ["www.politifact.com"]
    start_urls = ["https://www.politifact.com/videos"]

    custom_settings = { 'FEEDS':{'../../videos_info.json' : { 'format': 'json', 'overwrite': 'True'}} }

    def parse(self, response):
        video_links = response.xpath("//div[@class='m-video']/a/@href").extract()
        
        for link in video_links:
            full_link = "https://www.politifact.com" + link
            yield response.follow(full_link, callback=self.getVideoData)

    def getVideoData(self, response):
        video_info = Video_Info()

        video_info['title'] = response.xpath("//div[@class='m-statement__quote']/text()").extract()
        video_info['link'] = response.xpath("//div[@class='c-image']/iframe/@src").extract()
        video_info['categories'] = response.xpath("//li[@class='m-list__item']/a/span/text()").extract()
        video_info['description'] = response.xpath("//article[@class='m-textblock']/p/text()").extract()
        video_info['article_link'] = response.xpath("//div[@class='t-row__center']//article[@class='m-textblock']/p/a/@href").extract()
        video_info['contributers'] = response.xpath("//article[@class='m-textblock']//h3/following-sibling::div/a/text()").extract()

        yield video_info
