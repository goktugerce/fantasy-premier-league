from collections import defaultdict
from . import helpers, ownership

max_players = {'GK': 2, 'DEF': 5, 'MID': 5, 'FWD': 3}


def create_template_team(teams, players, effective=False, percentage=True, with_team=True, return_ids=False):
    """Create template team"""
    ownership_by_ids = ownership.get_ownership_stats(teams, players, effective, percentage, with_team, True)

    template = {'GK': [], 'DEF': [], 'MID': [], 'FWD': []}
    total_added = 0
    for player_id, owners in ownership_by_ids.items():
        player = helpers.find_player_by_id(players, player_id)
        if max_players[player.position] > len(template[player.position]):
            player.ownership = round(owners * 100, 1)
            template[player.position].append(player)
            total_added += 1

        if total_added == 15:
            break

    return template
