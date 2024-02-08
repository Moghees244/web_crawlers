# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Politifact.items import Video_Info
from Politifact.items import FactCheck_Info

class PolitifactPipeline:
    def process_item(self, item, spider):
        return item

class VideoPipeline:
    def process_item(self, item, spider):
        if isinstance(item, Video_Info):
            if 'title' in item:
                item['title'] = item['title'][0].replace('\n', '')
        return item
    
class FactCheckPipeline:
    def process_item(self, item, spider):
        if isinstance(item, FactCheck_Info):
            if 'personality' in item:
                item['personality'] = self.remove_endline(item['personality'])
            if 'statement' in item:
                item['statement'] = self.remove_endline(item['statement'])
            if 'venue' in item:
                item['venue'] = self.remove_endline(item['venue']).replace(':', '')
            if 'truth_meter' in item:
                item['truth_meter'] = self.get_truth_meter(item['truth_meter'])
            if 'image_urls' in item:
                item['image_urls'] = item['image_urls'].split("/")[-1]

        return item
    
    def remove_endline(self, data):
        return data.replace('\n', '')
    
    def get_truth_meter(self, url):
        word = url.split("/")[-1]   # Split the URL by "/" and get the name
        word = word.split(".")[0]      # remove extension
        
        if word == "tom_ruling_pof":
            return "Pants On Fire"
        if word == "tom_ruling_falso":
            return "Falso"

        parts = word.split("-")     # Split word by -
        # Capitalize the first letter of each word and join them together
        return ' '.join([part.capitalize() for part in parts[1:]])