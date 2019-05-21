from math import ceil
import logging

from . import utilities
from models import Player, LeagueStandings

PAGE_SIZE = 50.0
logging.getLogger().setLevel(logging.INFO)


def get_players(game='FPL'):
    """Return all players in the game, sorted by ownership"""
    players = []
    response = utilities.get_request(utilities.get_url('PLAYERS_METADATA_URL', game))

    for player in response:
        players.append(Player.Player(player))
    players.sort(key=lambda p: p.ownership, reverse=True)
    return players


def get_league(league_id, max_players=50, game='FPL'):
    """Return team ids in a league"""

    max_pages = int(ceil(max_players / PAGE_SIZE))
    team_ids = []

    for page in range(1, 1 + max_pages):
        response = utilities.get_request(
            utilities.get_url('LEAGUE_CLASSIC_STANDINGS_URL', game, league_id=league_id, page=page))
        league = LeagueStandings.LeagueStandings(response)
        team_ids += league.get_team_ids()
        logging.info('Page {}/{}'.format(page, max_pages))

    return team_ids[:max_players]
