import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class BaseParser:
    def __init__(self, base_url) -> None:
        self.base_url = base_url 
        self.headers = {}
        

    def _set_proxy(self):
        pass

    def __set_user_agent(self):
        ua = UserAgent()
        self.headers['User-Agent'] = ua.random

    def get(self, url):
        self.__set_user_agent()
        response = requests.get(url, headers=self.headers)
        return response.text

    def init_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup
        
    # полиморфные методы
    def get_links_data(self):
        raise NotImplementedError
    # полиморфные методы
    def get_details_data(self):
        raise NotImplementedError
