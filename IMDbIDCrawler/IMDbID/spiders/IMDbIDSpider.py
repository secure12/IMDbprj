#-*- coding: utf-8 -*-
import scrapy
import re


class IMDbIDSpider(scrapy.Spider):
    name = "IMDbIDSpider"
    allowed_domains = ["www.imdb.com"]

    def start_requests(self):

        start_year = 2006
        end_year = 2015
        rate = 1000
        # Do not use http://www.imdb.com/search/title?release_date=2006,2015&sort=year,asc&title_type=feature as the start urls.
        # Please generate urls year by year, i.e., the length of the following urls should be equal to 10.
        urls = [
            # your code here ...
            'http://www.imdb.com/search/title?count='+str(rate)+'&release_date='+str(year)+'&sort=year,asc&title_type=feature&view=simple' for year in range(start_year, end_year+1)
        ]
        # do not change the following lines
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        output_file = 'movie_ids06-15'
        # css selectors
        movie_info_selector = 'div.lister-item-content'
        movie_link_selector = 'div.lister-col-wrapper div.col-title span.lister-item-header'
        next_link_selector = 'a.lister-page-next.next-page::attr(href)'

        for movie_info in response.css(movie_info_selector):
            
            # use the movie_link_selector to extract the link of the movie
            # for example, the extracted movie link should be like /title/tt0407887/?ref_=adv_li_tt
            movie_id = re.findall('/title/(tt[0-9]*)/', movie_info.css(movie_link_selector).extract_first())[0]
            # regular expression to get the IMDb ID from the link /title/tt0407887/?ref_=adv_li_tt
            # for example, the extracted movid id should be like tt0407887
            with open(output_file, 'a') as f:
                f.write(movie_id + '\n')

        # deal with the next link
        next_link = response.css(next_link_selector).extract_first()
        # use the next_link_selector to extract the next link of the web page
        # for example, the extracted next link should be like "?release_date=2006,2006&sort=year,asc&title_type=feature&page=2&ref_=adv_nxt"

        # do not change the following lines
        if next_link is not None:
            next_link = response.urljoin(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
