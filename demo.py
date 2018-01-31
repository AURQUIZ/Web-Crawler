import scrapy

class GoogleSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.google.com/search?q=sql+injections+tutorial&oq=sql+injections+tutorial&aqs=chrome..69i57j0l5.641j0j4&sourceid=chrome&ie=UTF-8']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 a ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }


