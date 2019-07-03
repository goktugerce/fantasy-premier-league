from unittest import TestCase

from .files.mocks import *
from fantasy_premier_league.helpers.models import Team


class TestTeam(TestCase):

    def setUp(self):
        self.mock_team = mock_team_data
        self.mock_pick = mock_pick_data

    def test_team_initialization(self):
        team = Team.Team(self.mock_team)

        self.assertEqual(team.id, 6677)
        self.assertEqual(team.active_chip, 'Park the Bus')
        self.assertListEqual(team.picks, [Team.Picks(pick, 'Park the Bus') for pick in self.mock_team['picks']])

    def test_pick(self):
        pick = Team.Picks(self.mock_pick, 'Park the Bus')

        self.assertEqual(pick.player_id, 379)
        self.assertEqual(pick.position, 2)
        self.assertEqual(pick.captain, False)
        self.assertEqual(pick.vice_captain, False)
        self.assertEqual(pick.multiplier, 2)
        self.assertEqual(pick.benched, False)
