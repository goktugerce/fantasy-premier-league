import configparser
import requests
import sys

urls = configparser.ConfigParser()
urls.read('fantasy_premier_league/urls.ini')


def get_url(target, game='FPL', **kwargs):
    target_string = str(urls['DEFAULT'][target]).format(league_id=kwargs['league_id'], page=kwargs['page'])
    return '{}{}'.format(urls['DEFAULT'][game], target_string)


# noinspection PyBroadException
def get_request(url):
    response = requests.get(url)
    try:
        return response.json()
    except Exception:
        sys.exit('Game is being updated.')
