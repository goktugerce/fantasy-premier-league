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

    team = Team.Team(response, id=team_id)
    team_json = jsonpickle.encode(team, unpicklable=False)

    utilities.save_file(team_json, '{}/teams/{}/gw_{}.json'.format(game, team_id, gameweek))

    return team


def download_all_teams_histories(game, team_ids):
    """Download team picks one by one"""
    teams = []

    for counter, team_id in enumerate(team_ids):
        teams.append(download_team_history(game, team_id))
        logging.info('Downloaded Team History: {}/{}'.format(counter + 1, len(team_ids)))

    return teams


def download_team_history(game, team_id):
    """Download and parse team histories"""
    response = utilities.get_request(utilities.get_url('TEAM_HISTORY_URL', game, team_id=team_id))

    history = Team.History(response, id=team_id)
    history_json = jsonpickle.encode(history, unpicklable=False)

    utilities.save_file(history_json, '{}/history/{}.json'.format(game, team_id))
    return history


def read_team(game, team_id, gameweek):
    """Read single team id from the local storage"""
    team = utilities.read_file('{}/teams/{}/gw_{}.json'.format(game, team_id, gameweek))
    return team


def read_teams(game, team_ids, gameweek):
    """Read/download multiple teams from the local storage"""
    teams = []
    for team_id in team_ids:
        team = read_team(game, team_id, gameweek)
        if team is None:
            team = download_team_picks(game, team_id, gameweek)
            teams.append(team)
        else:
            teams.append(Team.Team(team=None, **team))
    return teams


def read_history(game, team_id):
    """Read single team history from the local storage"""
    team = utilities.read_file('{}/history/{}.json'.format(game, team_id))
    return team


def read_histories(game, team_ids):
    """Read/download multiple team histories from the local storage"""
    teams = []
    for team_id in team_ids:
        team = read_history(game, team_id)
        if team is None:
            team = download_team_history(game, team_id)
            teams.append(team)
        else:
            teams.append(Team.History(history=None, **team))
    return teams

