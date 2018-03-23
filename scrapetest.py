from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen("http://pythonscraping.com/pages/page1.html")
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


if __name__ == "__main__":
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title is None:
        print("Title could not be found")
    else:
        print(title)
