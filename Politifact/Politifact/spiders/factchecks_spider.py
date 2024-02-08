import scrapy
from Politifact.items import FactCheck_Info


class FactchecksSpiderSpider(scrapy.Spider):
    name = "factchecks_spider"
    allowed_domains = ["www.politifact.com"]
    start_urls = ["https://www.politifact.com/factchecks/"]

    custom_settings = {'FEEDS':{'../../factchecks.json' : { 'format': 'json', 'overwrite': 'True'}},}

    def parse(self, response):
        fact_links = response.xpath("//div[@class='m-statement__quote']/a/@href").extract()
        
        for link in fact_links:
            full_link = "https://www.politifact.com" + link
            yield response.follow(full_link, callback=self.getFactcheck)

        next_page = response.xpath("//section[@class='t-row ']//a[@class='c-button c-button--hollow']/@href").extract()
        button_text = response.xpath("//section[@class='t-row ']//a[@class='c-button c-button--hollow']/text()").extract()

        # previous and next page link had same classes and parents.
        if len(next_page) > 1:
            next_page_link = "https://www.politifact.com/factchecks/" + next_page[1]

        elif button_text[0] == "Next":
            next_page_link = "https://www.politifact.com/factchecks/" + next_page[0]
        else:
            return

        yield response.follow(next_page_link, callback=self.parse)

        
    
    def getFactcheck(self, response):
        fact_check = FactCheck_Info()
        
        fact_check['personality'] = response.xpath("//a[@class='m-statement__name']/text()").get()
        fact_check['image_urls'] = response.xpath("//div[@class='c-image']/img/@src").get()
        fact_check['venue'] = response.xpath("//div[@class='m-statement__desc']/text()").get()
        fact_check['statement'] = response.xpath("//div[@class='m-statement__quote']/text()").get()
        fact_check['truth_meter'] = response.xpath("//div[@class='m-statement__meter']//picture/img/@src").get()
        fact_check['categories'] = response.xpath("//li[@class='m-list__item']/a/span/text()").extract()
        fact_check['author'] = response.xpath("//div[@class='m-author__content copy-xs u-color--chateau']/a/text()").get()
        fact_check['publish_date'] = response.xpath("//div[@class='m-author__content copy-xs u-color--chateau']/span/text()").get()
        fact_check['description'] = response.xpath("//article[@class='m-textblock']/p/text()").extract()
        fact_check['sources'] = response.xpath("//section[@id='sources']//article/p/a/text()").extract()

        return fact_check
