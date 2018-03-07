import scrapy

class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    start_urls = ['https://www.google.com/search?q=sql+injections+tutorial', 'https://www.google.com/search?q=sql+injections+tutorial&start=10','https://www.google.com/search?q=sql+injections+tutorial&start=20'  ]

    def parse(self, response):
        SET_SELECTOR = '.g'
       	for brickset in response.css(SET_SELECTOR):
            
            NAME_SELECTOR = 'h3 a ::text'
            LINK_SELECTOR = 'a ::attr(href)'

            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'link': brickset.css(LINK_SELECTOR).extract_first(),
            }

#        for i in range(10):
        NEXT_PAGE_SELECTOR = 'pn ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:        
            yield scrapy.Request(
                   response.urljoin(next_page),
                   callback=self.parse
               )
