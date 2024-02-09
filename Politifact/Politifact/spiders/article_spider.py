import scrapy
from Politifact.items import Article_Info
from Politifact.utils import preprocess_image_urls


class ArticleSpiderSpider(scrapy.Spider):
    name = "article_spider"
    allowed_domains = ["www.politifact.com"]
    start_urls = ["https://www.politifact.com/article/"]

    custom_settings = {'FEEDS':{'../../articles.json' : { 'format': 'json', 'overwrite': 'True'}},}

    def parse(self, response):
        fact_links = response.xpath("//h3[@class='m-teaser__title']/a/@href").extract()
        
        for link in fact_links:
            full_link = "https://www.politifact.com" + link
            yield response.follow(full_link, callback=self.getArticle)

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

    
    def getArticle(self, response):
        article = Article_Info()
        
        article['title'] = response.xpath("//div[@class='m-statement__quote']/text()").get()        
        article['image_urls'] = preprocess_image_urls(response.xpath("//div[@class='c-image']/img/@src").extract())
        article['categories'] = response.xpath("//li[@class='m-list__item']/a/span/text()").extract()
        article['author'] = response.xpath("//div[@class='m-author__content copy-xs u-color--chateau']/a/text()").get()
        article['publish_date'] = response.xpath("//div[@class='m-author__content copy-xs u-color--chateau']/span/text()").get()
        article['description'] = response.xpath("//article[@class='m-textblock']/p/text()").extract()
        article['sources'] = response.xpath("//section[@id='sources']//article/p/a/text()").extract()

        return article
    
    
