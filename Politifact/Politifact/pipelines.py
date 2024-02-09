# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Politifact.items import Video_Info
from Politifact.items import FactCheck_Info
from Politifact.items import ScoreBoard
from Politifact.items import Article_Info
from Politifact.utils import remove_endline, get_truth_meter

class PolitifactPipeline:
    def process_item(self, item, spider):
        return item

class VideoPipeline:
    def process_item(self, item, spider):
        if isinstance(item, Video_Info):
            if 'title' in item:
                item['title'] = remove_endline(item['title'][0])
        return item
    
class FactCheckPipeline:
    def process_item(self, item, spider):
        if isinstance(item, FactCheck_Info):
            if 'personality' in item:
                item['personality'] = remove_endline(item['personality'])
            if 'statement' in item:
                item['statement'] = remove_endline(item['statement'])
            if 'venue' in item:
                item['venue'] = remove_endline(item['venue']).replace(':', '')
            if 'truth_meter' in item:
                item['truth_meter'] = get_truth_meter(item['truth_meter'])

        return item
    

class ScoreBoardPipeline:
    def process_item(self, item, spider):
        if isinstance(item, ScoreBoard):
            for attr in item:
                item[attr] = item[attr].replace("Checks", '')
        return item
    
class ArticlePipeline:
    def process_item(self, item, spider):
        if isinstance(item, Article_Info):
            if 'title' in item:
                item['title'] = remove_endline(item['title'])
        return item