import scrapy

class FilterSpider(scrapy.Spider):
    name = 'filterspider'
    start_urls = [
        'https://spotifycharts.com/regional/global/daily/latest',
        'https://spotifycharts.com/regional/global/weekly/latest',
        ]
    
    def parse(self, response):
        yield {
            # response.css('div.responsive-select').xpath('@data-type')[0].extract() : response.css('div.responsive-select')[0].css('ul li ::text').extract(),
            'country_name'  : response.css('div.responsive-select')[0].css('ul li ::text').extract(),
            'country_code'  : response.css('div.responsive-select')[0].css('ul li').xpath('@data-value').extract(),
            'date'          : response.css('div.responsive-select')[2].css('ul li ::text').extract(),
        }
