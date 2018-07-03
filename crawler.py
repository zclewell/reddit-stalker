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
        for container_div in page_soup.find_all('div',{"class":"Post__commentContainer"}):
            container_soup = BeautifulSoup(str(container_div),'html.parser')

            for username_div in container_soup.find_all('a'):
                print(BeautifulSoup(str(username_div),'html.parser').get_text())

            for text_div in container_soup.find_all('div',{'class':'md'}):
                text_soup = BeautifulSoup(str(text_div),'html.parser')
                for p in text_soup.find_all('p'):
                    print(BeautifulSoup(str(p),'html.parser').get_text())
                print('')
