from email import header
import requests
from time import sleep
from bs4 import BeautifulSoup

URL = "https://drom.ru"
CAR_URL = "https://avto.drom.ru"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.864 Yowser/2.5 Safari/537.36"
}

def html_response(url):
    try:
        response = requests.get(url, headers= headers)
        print('Данные со страницы {} получены...'.format(url))
        return response
    except ConnectionError or TimeoutError or ConnectionResetError:
        return None

def parse_soup(response):
    return BeautifulSoup(response, "lxml")

def search_class(soup, aoperator, aclass):
    return soup.find_all(aoperator, class_ = aclass)

def get_href(items):
    href = []
    for item in items:
        href.append(item.get('href'))
    return href

def get_one_href(item):
    return item.get('href')

def get_name(items):
    names = []
    for item in items:
        names.append(item.text)
    return names

def get_one_name(item):
    return item.text

def get_marks(items):
    marks = []
    for item in items:
        marks.append(item.text)
    return marks

def create_url_request(url, page, minprice, maxprice):
    return url + 'page{}/?minprice={}&maxprice={}'.format(page, minprice, maxprice)
    