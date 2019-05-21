import configparser
import requests
import json
import sys

urls = configparser.ConfigParser()
urls.read('fantasy_premier_league/urls.ini')


def get_url(target, main='FPL_URL'):
    return '{}{}'.format(urls['DEFAULT'][main], urls['DEFAULT'][target])


# noinspection PyBroadException
def get_request(url):
    response = requests.get(url)
    try:
        return json.loads(response.content.decode('utf-8'))
    except Exception:
        sys.exit('Game is being updated.')
