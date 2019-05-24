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


def convert_to_percentage(counts, length):
    """Convert dictionary of occurrences to percentages"""
    for key in counts:
        counts[key] /= length
    return counts
