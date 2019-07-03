import configparser
import json
import os
import requests
import shutil
import sys
from .urls import *

user_dir = os.path.expanduser("~") + "/.fpl"


def get_url(target, game='FPL', **kwargs):
    target_string = str(urls['DEFAULT'][target]).format(**kwargs)
    return '{}{}'.format(urls[game]['BASE_URL'], target_string)


# noinspection PyBroadException
def get_request(url):
    try:
        response = requests.get(url)
    except requests.exceptions.SSLError:
        response = requests.get(url, verify=False)
    try:
        return response.json()
    except Exception as e:
        sys.exit(e.message)


def save_file(content, file_path):
    """Save content to file path"""
    directory_name = os.path.split(file_path)[0]
    full_directory_path = os.path.join(user_dir, directory_name)

    if not os.path.isdir(full_directory_path):
        os.makedirs(full_directory_path, exist_ok=True)

    full_file_path = os.path.join(user_dir, file_path)

    # If instance is string, convert it to JSON so it does not escape quotes while dumping
    if isinstance(content, str):
        content = json.loads(content)

    with open(full_file_path, 'w') as outfile:
        json.dump(content, outfile, ensure_ascii=False)


def read_file(file_path):
    """Read content from file path"""
    full_file_path = os.path.join(user_dir, file_path)

    try:
        with open(full_file_path) as infile:
            content = json.load(infile)
            return content
    except OSError:
        return None


def get_portrait_url(player_id, game='FPL'):
    return urls[game]['PORTRAIT_URL'.format(game)].format(player_id=player_id)


def get_kit_url(team_id, game='FPL'):
    return urls[game]['KIT_URL'.format(game)].format(team_id=team_id)


# noinspection PyBroadException
def clear_directory():
    """Clear downloaded files in user directory."""
    try:
        shutil.rmtree(user_dir)
    except FileNotFoundError:
        pass

    os.makedirs(user_dir)
