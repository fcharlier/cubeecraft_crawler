# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from cubeecraft_crawler.items import CubeeItem


class CubeecraftSpider(CrawlSpider):
    name = "cubeecraft"
    allowed_domains = ["www.cubeecraft.com"]
    start_urls = ["http://www.cubeecraft.com/"]
    rules = (
        Rule(LinkExtractor(allow=("categories"))),
        Rule(LinkExtractor(allow=("/cubees/")), callback="parse_cubee"),
    )

    def parse_cubee(self, response):
        cubee_name = (
            response.css("div#cubee-show-header-wrapper>h3::text").get().strip("\n .")
        )

        self.logger.info("This is a cubee page for: %s" % cubee_name)

        cubee = CubeeItem()
        cubee["rsp"] = response
        yield cubee
