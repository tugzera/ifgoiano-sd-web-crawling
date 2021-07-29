import scrapy
import csv

class Spider(scrapy.Spider):
    name = 'Globo'
    allowed_domains = ['sof.to']
    start_urls = ['https://sof.to/']

    def __init__(self):
        self.links = {}
        with open('graph_nodes.csv', 'w', encoding='UTF8') as f:
            header = ["ID", "Label"]
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            f.close()


    def parse(self, response):
        with open('graph_nodes.csv', 'a', encoding='UTF8') as f:
            data = [response.url, response.url]
            writer = csv.writer(f)
            # write the header
            writer.writerow(data)
            f.close()
        for href in response.css('a::attr(href)'):
            if "https://" not in href.extract() :
                self.links["Source"] = response.url
                self.links["Target"] = f"https://sof.to/{href.extract()}"
                yield self.links
            yield response.follow(href, self.parse)
        # return self.links
            # if(f"{response.url}" in self.links):
            #     # print(self.links[""+ response.url+""])
            #     self.links[""+ response.url+""].append(href.extract())
            # else:
            #     self.links[""+ response.url+""] = [href.extract()]
            #     # print(self.links[""+ response.url+""])
            # parsedFile = json.dumps(self.links)
            # with open('output.json', "w") as myfile:
            #     myfile.write(parsedFile)
