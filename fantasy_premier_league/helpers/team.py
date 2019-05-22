from .. import utilities
from .models import Team


def download_team_picks(game, team_id, gameweek):
    """Download and parse team picks"""
    response = utilities.get_request(
        utilities.get_url('TEAM_ENTRY_URL', game, team_id=team_id, gameweek=gameweek))

    team = Team.Team(response)
    return team
