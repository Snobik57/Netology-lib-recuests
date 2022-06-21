import requests
from pprint import pprint

url_sh = 'https://akabab.github.io/superhero-api/api/all.json'


def get_id(url, *names):
    taken_superheroes = {}
    response = requests.get(url)
    all_superheros = response.json()
    for name in names:
        for sh in all_superheros:
            if sh['name'] == name:
                taken_superheroes.setdefault(name, {'id': sh['id'], 'intelligence': sh['powerstats']['intelligence']})
    # pprint(response.json())
    return taken_superheroes


if __name__ == '__main__':
    pprint(get_id(url_sh, 'Hulk', 'Captain America', 'Thanos'))
