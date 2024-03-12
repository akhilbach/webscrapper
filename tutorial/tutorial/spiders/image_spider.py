import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = ['https://www.ajio.com/pyos-women-geometric-print-saree-with-contrast-border/p/466755255_multi']  # Change this URL to the desired starting point

    def parse(self, response):
        # Extract image URLs from the response
        image_urls = response.css('img::attr(src)').extract()

        for img_url in image_urls:
            # Some URLs might be relative, so we need to make them absolute
            img_url = response.urljoin(img_url)
            
            # Request each image URL and pass it to the 'parse_image' method
            yield scrapy.Request(img_url, callback=self.parse_image)

    def parse_image(self, response):
        # Get the filename from the URL
        filename = response.url.split('/')[-1]

        # Save the image to the filesystem, change path as needed
        with open(f'/home/akhilbach/github.com/akhilbach/webscrapper/tutorial/tutorial/spiders/{filename}', 'wb') as f:
            f.write(response.body)
