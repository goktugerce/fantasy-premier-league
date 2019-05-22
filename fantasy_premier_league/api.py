from .helpers import player, league


def get_players(game='FPL'):
    """Return all players in the game, sorted by ownership"""
    players = player.get_players(game)
    return players


def get_league(league_id, max_players=50, game='FPL', overwrite=True):
    """Return team ids in a league"""

    if overwrite:
        team_ids = league.get_league_team_ids(league_id, max_players, game)
    else:
        team_ids = league.read_team_ids(league_id, max_players, game)

    return team_ids[:max_players]
