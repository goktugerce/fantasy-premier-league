from collections import defaultdict
from . import helpers


def get_ownership_stats(teams, players, effective=False, percentage=True, with_team=True, return_ids=False):
    """Find captaincy stats for players"""
    ownership_by_id = count_by_ids(teams, effective)
    ownership_by_name = helpers.map_names(ownership_by_id, players, with_team)

    if percentage:
        total_teams = len(teams)
        ownership_by_id = helpers.convert_to_percentage(ownership_by_id, total_teams)
        ownership_by_name = helpers.convert_to_percentage(ownership_by_name, total_teams)

    if return_ids:
        return helpers.sort_by_value(ownership_by_id)

    return helpers.sort_by_value(ownership_by_name)


def get_effective_ownership_stats(teams, players, percentage=True, with_team=True, return_ids=False):
    """Get effective ownership for players, counting captains and chips"""
    return get_ownership_stats(teams, players, True, percentage, with_team, return_ids)


def count_by_ids(teams, effective=False):
    """Count ownership by ids"""
    ownership_by_id = defaultdict(int)
    for team in teams:
        for pick in team.picks:
            if effective:
                multiplier = 0 if pick.benched else pick.multiplier
            else:
                multiplier = 1
            ownership_by_id[pick.player_id] += multiplier

    return ownership_by_id
