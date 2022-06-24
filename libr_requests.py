import requests
import os
import datetime as DT
import time
from pprint import pprint


# Task 1
class SuperHero:

    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.stats = {}

    def _get_link_all_superhero(self):

        return 'https://akabab.github.io/superhero-api/api/'

    def get_id(self):
        response = requests.get(self._get_link_all_superhero() + 'all.json')
        all_superheros = response.json()
        for superhero in all_superheros:
            if self.name == superhero['name']:
                self.id = str(superhero['id'])
        print(f'id получен: {self.id}')

    def get_stats(self):
        response = requests.get(self._get_link_all_superhero() + 'powerstats/' + self.id + '.json')
        self.stats = response.json()
        print('Характеристики получены')


def get_cleverest(*superheros):
    id = {}
    intelligence_sh = {}
    for superhero in superheros:
        intelligence = superhero.stats['intelligence']
        intelligence_sh.setdefault(superhero.name, intelligence)
        id.setdefault(superhero.name, superhero.id)
    the_cleverest = max(intelligence_sh, key=intelligence_sh.get)

    return f'Самый умный супергерой - {id[the_cleverest]}: {the_cleverest}\n' \
           f'Его уровень интеллекта - {intelligence_sh[the_cleverest]}'


halk = SuperHero('Hulk')
cap = SuperHero('Captain America')
thanos = SuperHero('Thanos')


# Task 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self):
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
        response_href = self._get_upload_link()
        href = response_href.get('href', '')
        response = requests.put(href, data=open(path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загрузка завершена')


# Task 3

today = DT.date.today()
from_day = today - DT.timedelta(2)


def get_questions(todate, fromdate, tag: str):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'site': 'Stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': f'{fromdate}',
        'todate': f'{todate}',
        'tagged': tag
    }
    response = requests.get(url, params=params)
    resp = response.json()
    questions = {}
    for items in resp['items']:
        unix_date = items['last_activity_date']
        date = DT.datetime.utcfromtimestamp(unix_date).strftime('%Y-%m-%d')
        questions.setdefault(items['question_id'], {date: items['link']})

    return questions


if __name__ == '__main__':

# Task 1
    halk.get_id()
    cap.get_id()
    thanos.get_id()
    halk.get_stats()
    cap.get_stats()
    thanos.get_stats()
    print(get_cleverest(halk, cap, thanos))

# Task 2
    # # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_file = os.path.join(os.getcwd(), 'homework8')
    # TOKEN = ''
    # yandex_disk = YaUploader(TOKEN)
    # yandex_disk.upload_file(path_to_file)

# Task 3
    # pprint(get_questions(today, from_day, 'python'))
