import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html)
for link in soup.find("div", {"id":"bodyContent"}).findAll("a",
                                                         href=re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print(link.attrs['href'])