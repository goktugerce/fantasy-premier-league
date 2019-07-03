from unittest import TestCase

from .files.mocks import *
from fantasy_premier_league.helpers.models import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.mock_player = mock_player_data

    def test_player_initialization(self):
        player = Player.Player(self.mock_player, 'ALLSVENSKAN')

        self.assertEqual(player.id, 60)
        self.assertEqual(player.code, 102046)
        self.assertEqual(player.name, 'Tankovic')
        self.assertDictEqual(player.team, {'short_name': 'HAM', 'name': 'Hammarby IF'})
        self.assertEqual(player.team_id, 1987)
        self.assertEqual(player.position, 'MID')
        self.assertEqual(player.ownership, 44.4)
        self.assertEqual(player.photo, '102046.jpg')
