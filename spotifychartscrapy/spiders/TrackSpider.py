import scrapy
import sys

class TrackSpider(scrapy.Spider):
    name = 'trackspider'
    
    def start_requests(self):
        urls = [
            'https://spotifycharts.com/regional/global/daily/latest',
        ]
        print(sys.argv[1])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        for tr in response.css('table.chart-table tbody tr'):
            yield {
                'position'  : tr.css('td.chart-table-position ::text').extract_first(),
                'track'     : tr.css('td.chart-table-track strong ::text').extract_first(),
                'by'        : tr.css('td.chart-table-track span ::text').extract_first(),
                'streams'   : tr.css('td.chart-table-streams ::text').extract_first()
            }