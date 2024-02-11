import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.altnews.in"]
    start_urls = ["https://www.altnews.in/"]

    custom_settings = {'FEEDS':{'../../altnews.json' : { 'format': 'json', 'overwrite': 'True'}},}

    def parse(self, response):
        # Extracting visible text content
        text_content = response.xpath('//*[not(self::script) and not(self::style)]/text()').getall()
        image_urls = response.css('img::attr(src)').extract()
        audio_urls = response.css('audio::attr(src)').extract()
        video_urls = response.css('video::attr(src)').extract()
        yield {
            'url': response.url,
            'text_content': text_content,
            'image_urls': image_urls,
            'audio_urls': audio_urls,
            'video_urls': video_urls
        }

         # Iterate over each audio URL and download the file
        for url in audio_urls:
            yield scrapy.Request(url, callback=self.save_audio)

    def save_audio(self, response):
        # Extract the filename from the URL
        filename = response.url.split('/')[-1]

        # Save the audio file to disk
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')

