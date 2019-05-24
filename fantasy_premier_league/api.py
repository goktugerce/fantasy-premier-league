from .helpers import player, league, team


def get_players(game='FPL'):
    """Return all players in the game, sorted by ownership"""
    players = player.download_players(game)
    return players


def get_league(league_id, max_players=50, game='FPL', overwrite=True):
    """Return team ids in a league"""

    if overwrite:
        team_ids = league.get_league_team_ids(league_id, max_players, game)
    else:
        team_ids = league.read_team_ids(league_id, max_players, game)

    return team_ids[:max_players]


def get_league_team_picks(team_ids, gameweek, game='FPL', overwrite=False):
    """Get all teams' picks for given gameweek"""

    if overwrite:
        return team.download_all_teams_picks(game, team_ids, gameweek)

    return team.read_teams(game, team_ids, gameweek)


def get_team_picks(team_id, gameweek, game='FPL'):
    """Return team information and picks for the given gameweek"""
    team_object = team.download_team_picks(game, team_id, gameweek)
    return team_object
