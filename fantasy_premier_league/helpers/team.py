import logging

import jsonpickle

from .. import utilities
from .models import Team

logging.getLogger().setLevel(logging.INFO)


def download_all_teams_picks(game, team_ids, gameweek):
    """Download team picks one by one"""
    teams = []

    for counter, team_id in enumerate(team_ids):
        teams.append(download_team_picks(game, team_id, gameweek))
        logging.info('Downloaded Team Picks: {}/{}'.format(counter + 1, len(team_ids)))

    return teams


def download_team_picks(game, team_id, gameweek):
    """Download and parse team picks"""
    response = utilities.get_request(
        utilities.get_url('TEAM_ENTRY_URL', game, team_id=team_id, gameweek=gameweek))

    team = Team.Team(response)
    team_json = jsonpickle.encode(team, unpicklable=False)

    utilities.save_file(team_json, '{}/teams/{}/gw_{}.json'.format(game, team_id, gameweek))

    return team