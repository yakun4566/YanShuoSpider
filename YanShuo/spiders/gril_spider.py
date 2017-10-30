import scrapy

class GrilSpider(scrapy.Spider):
    name = "yanshuo"
    allowed_domains = ["yanshuo.me"]
    start_urls = [
        "http://www.yanshuo.me/r/meizi",
        "http://www.yanshuo.me/r/meizi/hot",
        "http://www.yanshuo.me/r/meizi/week"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)