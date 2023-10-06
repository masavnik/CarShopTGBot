import requests
import json
from bs4 import BeautifulSoup as bs
from random import randint
from data import config


class AutoRequest:
    def __init__(self):
        self.link: list = []
        self.auto_list: list = []
        self.url: str = config.url

    def requests_get(self):
        '''Подает запрос на сайт'''
        response = requests.get(self.url)
        return bs(response.text, 'lxml')

    def link_cleaning(self) -> list:
        '''
        Метод чистит теги и возвращает список ссылок
        изображений на автомобили по 4 шт
        на каждый автомобиль
        '''
        container_link = self.requests_get().findAll(class_='lazyload')
        for i in container_link:
            get_link = i.get("data-src")
            if get_link.startswith('https:'):
                self.link.append(get_link)
        return self.link

    def auto_cleaning(self) -> list:
        '''
        -Метод создает список из словарей с данными автомобилей
        -Ключ PRICE имеет рандомное знаечение, так как на сайте
        нет цен на автомобили
        '''
        container_auto = self.requests_get().findAll('div', class_='text')
        for i_auto in container_auto:
            self.auto_list.append({'AUTO': i_auto.find(class_="title").text,
                                   'RUN': i_auto.find(class_="run").text,
                                   'ENGINE': i_auto.find(class_="engine").text,
                                   'YEAR_OF_ISSUE': i_auto.find(class_="props").find().text,
                                   'FUEL': ''.join(i_auto.find(class_="props").text.split(','))[17:36],
                                   'LINK': [self.link[i:i + 4] for i in range(0, len(self.link_cleaning()), 4)]
                                   [len(self.auto_list)],
                                   'PRICE': '{:,}'.format(
                                   (round(randint(2000000, 10000000), -4))
                                   ).replace(',', ' ') + ' рублей'
                                   }
                                  )
        return self.auto_list


auto = AutoRequest()


def vehicle_data_recording():
    with open('data/parser.json', 'w') as file:
        json.dump(auto.auto_cleaning(), file, indent=4, ensure_ascii=False)