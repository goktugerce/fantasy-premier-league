from collections import defaultdict
from . import helpers


def get_captaincy_stats(teams, players, percentage=True):
    """Find captaincy stats for teams"""
    captaincy_by_id = count_by_ids(teams)
    captaincy_by_name = helpers.map_names(captaincy_by_id, players, with_team=True)

    if percentage:
        total_teams = len(teams)
        captaincy_by_name = helpers.convert_to_percentage(captaincy_by_name, total_teams)

    return helpers.sort_by_value(captaincy_by_name)


def count_by_ids(teams):
    """Count captains by ids"""
    captaincy_by_id = defaultdict(int)
    for team in teams:
        captain_id = helpers.find_captain_id(team.picks)
        captaincy_by_id[captain_id] += 1

    return captaincy_by_id
