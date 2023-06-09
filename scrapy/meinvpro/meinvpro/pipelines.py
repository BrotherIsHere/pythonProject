# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class MeinvproPipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class picpipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['pic'])

    def file_path(self, request, response=None, info=None, *, item=None):
        pic_name=request.url.split('/')[-1]
        return pic_name
    def item_completed(self, results, item, info):
        return item
