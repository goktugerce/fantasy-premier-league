from math import ceil
import logging

from .. import utilities
from .models import League

logging.getLogger().setLevel(logging.INFO)

PAGE_SIZE = 50.0


def get_league_team_ids(league_id, max_players, game):
    """Download team ids in the league"""
    max_pages = int(ceil(max_players / PAGE_SIZE))
    team_ids = []

    for page in range(1, 1 + max_pages):
        response = utilities.get_request(
            utilities.get_url('LEAGUE_CLASSIC_STANDINGS_URL', game, league_id=league_id, page=page))
        league = League.LeagueStandings(response)
        league_team_ids = league.get_team_ids()

        team_ids += league_team_ids

        if len(league_team_ids) < PAGE_SIZE:
            logging.info('No more teams in the league')
            break
        else:
            logging.info('Page {}/{}'.format(page, max_pages))

    utilities.save_file(team_ids, '{}/league/{}/team_ids.json'.format(game, league_id))
    return team_ids


def read_team_ids(league_id, max_players, game):
    """Read team ids from the local storage"""
    team_ids = utilities.read_file('{}/league/{}/team_ids.json'.format(game, league_id))

    if team_ids is None or len(team_ids) < max_players:
        team_ids = get_league_team_ids(league_id, max_players, game)

    return team_ids[:max_players]
