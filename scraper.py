import scrapy
from scrapy.crawler import CrawlerProcess

class GetConfTalks(scrapy.Spider):
    name = 'get_conf_talks'
    allowed_domains = ['churchofjesuschrist.org']
    download_delay = 2

    def __init__(self):
      self.start_year = 1974
      self.end_year = 2020
    
    def start_requests(self):
      apr = ['https://www.churchofjesuschrist.org/study/general-conference/' + str(i) + '/04?lang=eng' for i in range(self.start_year,self.end_year+1)]
      octo = ['https://www.churchofjesuschrist.org/study/general-conference/' + str(i) + '/10?lang=eng' for i in range(self.start_year,self.end_year+1)]
      urls = apr + octo
      for url in urls:
        yield scrapy.Request(url=url, callback=self.get_article_links)

    def get_article_links(self, response):
      urls = response.css("ul.doc-map").css("a::attr(href)").getall()
      for url in urls:
        url = 'https://www.churchofjesuschrist.org' + url
        yield scrapy.Request(url=url, callback=self.get_text)

    def get_text(self, response):
      title = response.css('header').css('h1::text').get()
      author = response.css('div.byline').css('#p1::text').get()
      text = " ".join(response.css('div.body-block').css('p::text').getall())
      year = response.request.url[61:65]
      month = response.request.url[66:68]
      yield {"title":title, "author":author, "year": year, "month":month, "text":text}


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    "FEEDS": {
        "talks.csv": {"format": "csv"}
    }
})

process.crawl(GetConfTalks)
process.start()
