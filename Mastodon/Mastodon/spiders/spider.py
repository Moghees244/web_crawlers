import scrapy
import json
from Mastodon.items import Post_Info, Media_Attachment


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["mastodon.social"]
    start_urls = ["https://mastodon.social/explore"]

    custom_settings = {'FEEDS':{'../../posts.json' : { 'format': 'json', 'overwrite': 'True'}},}

    def parse(self, response):
        page = "https://mastodon.social/api/v1/trends/statuses?offset="
 
        for offset in range(1):
            next_page = page + str(offset)
            yield scrapy.Request(next_page, callback=self.parse_data)

    def parse_data(self, response):
        if response:
            data = json.loads(response.body)
            for post in data:
                yield self.get_post_info(post)

    def get_post_info(self, data):
        post_info = Post_Info()

        post_info['id'] = data['id']
        post_info['username'] = data['account']['username']
        post_info['created_at'] = data['created_at']
        post_info['sensitive'] = data['sensitive']
        post_info['language'] = data['language']
        post_info['url'] = data['url']
        post_info['replies_count'] = data['replies_count']
        post_info['reblogs_count'] = data['reblogs_count']
        post_info['favourites_count'] = data['favourites_count']
        post_info['content'] = data['content']
        post_info['mentions'] = data['mentions']
        post_info['tags'] = data['tags']
        post_info['card'] = data['card']
        post_info['poll'] = data['poll']

        media_attachment_data, images = [], []
        for attachment in data.get('media_attachments'):
            media_attachment = Media_Attachment()
            media_attachment["media_type"] = attachment['type']
            media_attachment["image_urls"] = attachment['url']
            images.append(attachment['url'])
            media_attachment["description"] = attachment['description']
            media_attachment_data.append(media_attachment)
        
        post_info['media'] = media_attachment_data
        post_info['image_urls'] = images

        return post_info