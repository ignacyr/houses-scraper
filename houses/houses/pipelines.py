# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class HousesPipeline:
    def process_item(self, item, spider):
        house_json = json.dumps(item, indent=4)
        with open('houses.json', 'a') as f:
            f.write(house_json + ',\n')
        return item
