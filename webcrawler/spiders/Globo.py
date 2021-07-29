import scrapy
import json
import sys

class GloboSpider(scrapy.Spider):
    name = 'Globo'
    allowed_domains = ['sof.to']
    start_urls = ['https://sof.to/']

    def __init__(self):
        self.links = {}


    def parse(self, response):
        for href in response.css('a::attr(href)'):
            if(f"{response.url}" in self.links):
                # print(self.links[""+ response.url+""])
                self.links[""+ response.url+""].append(href.extract())
            else:
                self.links[""+ response.url+""] = [href.extract()]
                # print(self.links[""+ response.url+""])
            yield response.follow(href, self.parse)
            parsedFile = json.dumps(self.links)
            with open('output.json', "w") as myfile:
                myfile.write(parsedFile)
