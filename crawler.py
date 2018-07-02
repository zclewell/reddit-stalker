from scrapy import log # This module is useful for printing out debug information
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from bs4 import BeautifulSoup

import json

BASE_URL = "https://www.reddit.com/user/"
usernames = json.load(open('./usernames.json'))

class RedditSpider(BaseSpider):
    name = 'reddit-spider'
    start_urls = []
    for username in usernames:
        start_urls.append(BASE_URL + username)

    def parse(self, response):
        # print(response.body)
        page_soup = BeautifulSoup(response.body,'html.parser')
        for div in page_soup.find_all('div',{"class":"md"}):
            div_soup = BeautifulSoup(str(div),'html.parser')
            for p in div_soup.find_all('p'):
                print(BeautifulSoup(str(p),'html.parser').get_text())
            print('')
        # hxs = HtmlXPathSelector(response)
        # for div in hxs.select('//div').extract():
        #     print(div)
        #
        # # print(response.body)
        # # for url in hxs.select('//a/@href').extract():
        # #     print(url)
