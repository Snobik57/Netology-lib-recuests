import requests
import os
import datetime as DT
import time
from pprint import pprint


# Task 1

url_sh = 'https://akabab.github.io/superhero-api/api/all.json'


def get_cleverest(url, *names):
    taken_superheroes = {}
    response = requests.get(url)
    all_superheros = response.json()
    for name in names:
        for sh in all_superheros:
            if sh['name'] == name:
                taken_superheroes.setdefault(name, sh['powerstats']['intelligence'])
    the_cleverest = max(taken_superheroes, key=taken_superheroes.get)
    return f'Самый умный супергерой - {the_cleverest}. Его уровень интеллекта - {taken_superheroes[the_cleverest]}'


# if __name__ == '__main__':
#     pprint(get_cleverest(url_sh, 'Hulk', 'Captain America', 'Thanos'))


# Task 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }
        params = {'path': '/Homework8 by Timur Gusev.txt', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        response_href = self.get_upload_link()
        href = response_href.get('href', '')
        response = requests.put(href, data=open(path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загрузка завершена')


# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = os.path.join(os.getcwd(), 'homework8')
#     TOKEN = ''
#     yandex_disk = YaUploader(TOKEN)
#     yandex_disk.upload_file(path_to_file)


# Task 3

today = DT.datetime.today()
from_day = today - DT.timedelta(2)
unix_today = int(today.timestamp())
unix_from_day = int(from_day.timestamp())


def get_questions():
    url = 'https://api.stackexchange.com/2.3/questions/'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'fromdate': f'{unix_from_day}',
        'today': f'{unix_today}',
        'tagged': 'python'
    }
    response = requests.get(url, params=params)
    resp = response.text
    return resp


if __name__ == '__main__':
    pprint(get_questions())
