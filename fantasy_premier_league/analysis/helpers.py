import collections


def find_captain_id(picks):
    """Find captain's id among picks"""
    for pick in picks:
        if pick.captain:
            return pick.player_id

    return None


def find_player_by_id(players, player_id):
    """Find player by id among players"""
    for player in players:
        if player.id == player_id:
            return player

    return None


def get_player_position(players, player_id):
    player = find_player_by_id(players, player_id)

    return player.position if player is not None else None


def convert_to_percentage(counts, length):
    """Convert dictionary of occurrences to percentages"""
    for key in counts:
        counts[key] /= length
    return counts


def map_names(occurrences, players, with_team=False):
    """Map player ids to names"""
    occurrences_by_name = {}
    for player_id, occurrence in occurrences.items():
        player = find_player_by_id(players, player_id)

        name = player.name
        if with_team:
            name += ' ({})'.format(player.team['short_name'])

        occurrences_by_name[name] = occurrence

    return occurrences_by_name


def sort_by_value(dictionary):
    """Sort dictionary by value"""
    return collections.OrderedDict(sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True))
