# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Mastodon.items import Account_Info, Post_Info
from Mastodon.utils import remove_endline, remove_tags

class MastodonPipeline:
    def process_item(self, item, spider):
        return item
    
class AccountPipeline:
       def process_item(self, item, spider):
            if isinstance(item, Account_Info):
                if 'note' in item:
                    item['note'] = remove_tags(item['note'])

            if 'fields' in item:
                for field in item['fields']:
                    field['value'] = remove_tags(field['value'])
        
            return item

class PostPipeline:
    def process_item(self, item, spider):
        if isinstance(item, Post_Info):
            if 'content' in item:
                item['content'] = remove_tags(item['content'])
            
            if 'description' in item:
                item['description'] = remove_endline(item['description'])
        return item