import scrapy

class TrainSpider(scrapy.Spider):
    name = "train"
    start_urls = ['http://bocznica.eu/']

    def parse(self, response):
        for row in response.xpath('//*[@class="zestawieniaTable"]//tr')[1:]:
            if "Warszawa" not in ''.join([i for i in row.css('td.relacjaTd::text')[0].extract() if not i.isdigit()]).strip().replace("-", "_").replace(" ", "").replace(":", "").replace("(", "").replace(")", "").replace("/", ""):
                continue
            elif "Sochaczew" not in ''.join([i for i in row.css('td.relacjaTd::text')[0].extract() if not i.isdigit()]).strip().replace("-", "_").replace(" ", "").replace(":", "").replace("(", "").replace(")", "").replace("/", ""):
                continue              
            else:
                yield {
                    'Number': row.xpath('td//text()')[0].extract(),
                    'Type': row.xpath('td//text()')[1].extract().strip(),
                    'Name': row.css('b::text').extract(),
                    'Route': ''.join([i for i in row.css('td.relacjaTd::text')[0].extract() if not i.isdigit()]).strip().replace("-", "_").replace(" ", "").replace(":", "").replace("(", "").replace(")", "").replace("/", ""),
                }
