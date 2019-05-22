import configparser
import json
import os
import requests
import sys

urls = configparser.ConfigParser()
urls.read('fantasy_premier_league/urls.ini')
user_dir = os.path.expanduser("~") + "/.fpl"


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


def save_file(content, file_path):
    """Save content to file path"""
    directory_name = os.path.split(file_path)[0]
    full_directory_path = os.path.join(user_dir, directory_name)

    if not os.path.isdir(full_directory_path):
        os.makedirs(full_directory_path, exist_ok=True)

    full_file_path = os.path.join(user_dir, file_path)
    with open(full_file_path, 'w') as outfile:
        json.dump(content, outfile, ensure_ascii=False)


def read_file(file_path):
    """Read content from file path"""
    full_file_path = os.path.join(user_dir, file_path)

    with open(full_file_path) as infile:
        content = json.load(infile)
        return content
