from collections import defaultdict
from . import helpers


def get_weekly_chip_usage(teams, percentage=True):
    """Get weekly chip usage for teams"""
    chips_used = defaultdict(int)
    for team in teams:
        chips_used[team.active_chip] += 1

    if percentage:
        total_teams = len(teams)
        chips_used = helpers.convert_to_percentage(chips_used, total_teams)

    return helpers.sort_by_value(chips_used)
