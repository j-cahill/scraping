from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

pages = set()
def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org/' + page_url)
    soup = BeautifulSoup(html)
    for link in soup.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)

get_links("")

"""    
links = get_links('/wiki/Kevin_Bacon')
while links:
    new_article = links[random.randint(0, len(links)-1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)
"""
