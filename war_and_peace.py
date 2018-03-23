from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, "lxml")
name_list = soup.findAll("span", {"class": "green"})
for name in name_list:
    print(name.get_text())
