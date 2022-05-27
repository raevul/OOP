import requests
from bs4 import BeautifulSoup

URL = 'https://www.kinopoisk.ru'


def get_html(url):
    response = requests.get(url)
    return response.text


def 