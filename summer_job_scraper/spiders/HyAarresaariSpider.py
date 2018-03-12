import scrapy


class AarresaariSpider(scrapy.Spider):
    name = "scrape"

    def start_requests(self):
        urls = [
            'https://www.aarresaari.net//',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'scrape-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
