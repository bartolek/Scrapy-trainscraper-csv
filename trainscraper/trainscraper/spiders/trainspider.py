import scrapy
#from scrapy.crawler import CrawlerProcess

class TrainSpider(scrapy.Spider):
    name = "train"
    start_urls = ['http://bocznica.eu/trains']
    allowed_domains = ['bocznica.eu']

    #http://bocznica.eu/stats/42102

    def parse(self, response):
        for row in response.xpath('//table//tr')[1:]:
            print(row)
            #print(row.xpath('td//a').attrib['href'])
            if len(row.xpath('td//text()')[1].extract().split()) > 2:
                yield {
                    'Number': row.xpath('td//text()')[0].extract(),
                    'Train ID': row.xpath('td//text()')[1].extract().split()[1],
                    'Train Name': (row.xpath('td//text()')[1].extract().split()[2]),
                    "Route": row.xpath('td//text()')[2].extract() + "-" + row.xpath('td//text()')[3].extract(),
                    "Average delay": row.xpath('td//text()')[4].extract().split(),
                }
            else:
                yield {
                    'Number': row.xpath('td//text()')[0].extract(),
                    'Train ID': row.xpath('td//text()')[1].extract().split()[1],
                    'Train Name': '',
                    "Route": row.xpath('td//text()')[2].extract() + "-" + row.xpath('td//text()')[3].extract(),
                    "Average delay": row.xpath('td//text()')[4].extract().split(),
                }

            follow_train = 'http://bocznica.eu' + row.xpath('td//a').attrib['href']
            print(follow_train)
            yield response.follow(follow_train, callback=self.parse_second)

    def parse_second(self, response):
        print('test')



#process = CrawlerProcess(settings = {
#    'FEED_URI': 'trains.json',
#    'FEED_FORMAT': 'json'
#})

#process.crawl(TrainSpider)
#process.start()
