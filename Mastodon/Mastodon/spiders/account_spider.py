import scrapy
import json
from Mastodon.items import Account_Info

class AccountSpiderSpider(scrapy.Spider):
    name = "account_spider"
    allowed_domains = ["mastodon.social"]
    start_urls = ["https://mastodon.social/explore"]

    custom_settings = {'FEEDS':{'../../accounts.json' : { 'format': 'json', 'overwrite': 'True'}},}

    def parse(self, response):
        page = "https://mastodon.social/api/v1/trends/statuses?offset="
 
        for offset in range(1):
            next_page = page + str(offset)
            yield scrapy.Request(next_page, callback=self.parse_data)

    def parse_data(self, response):
        if response:
            data = json.loads(response.body)
            for account in data:
                yield self.get_account_info(account)

    def get_account_info(self, data):
        account_info = Account_Info()

        account_info['username'] = data['account']['username']
        account_info['display_name'] = data['account']['display_name']
        account_info['note'] = data['account']['note']
        account_info['url'] = data['account']['url']
        account_info['avatar'] = data['account']['avatar']
        account_info['followers_count'] = data['account']['followers_count']
        account_info['following_count'] = data['account']['following_count']
        account_info['statuses_count'] = data['account']['statuses_count']
        account_info['fields'] = data['account']['fields']
        
        return account_info