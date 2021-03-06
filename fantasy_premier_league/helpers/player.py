from .. import utilities
from .models import Player


def download_players(game):
    """Download latest player information."""
    response = utilities.get_request(utilities.get_url('BOOTSTRAP_STATIC_URL', game))
    players = []

    for player in response['elements']:
        players.append(Player.Player(player, game=game))
    players.sort(key=lambda p: p.ownership, reverse=True)
    return players
