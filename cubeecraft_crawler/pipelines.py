# -*- coding: utf-8 -*-

# from scrapy.exceptions import DropItem
import logging
import re
from scrapy import FormRequest
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse, parse_qs


class CubeePipeline(FilesPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def file_path(self, request, response=None, info=None, *, item=None):
        if not response:
            return None
        try:
            qs = parse_qs(urlparse(response.url).query)
            filenames = re.findall(
                'filename="(.*?)";', qs["response-content-disposition"][0]
            )
            return filenames[0]
        except Exception as e:
            logging.exception(e)
            raise e

    def get_media_requests(self, item, info):
        return [
            FormRequest.from_response(
                item["rsp"],
                formcss="div.cubee-download-buttons-wrapper>form.button_to",
            ),
        ]

    def process_item(self, item, spider):
        super().process_item(item, spider)
