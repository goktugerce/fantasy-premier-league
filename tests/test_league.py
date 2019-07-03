from unittest import TestCase

from .files.mocks import *
from fantasy_premier_league.helpers.models import League


class TestLeague(TestCase):
    def setUp(self):
        self.mock_league = mock_league_data
        self.mock_entry = mock_league_entry

    def test_league_standings(self):
        league = League.LeagueStandings(self.mock_league)

        self.assertEqual(league.name, 'Overall')
        self.assertEqual(league.id, 47)
        self.assertListEqual(league.get_team_ids(),
                             [6677, 440, 16762, 4215, 7010, 10606, 12331, 10221, 5499, 8140, 24194, 11088, 18028, 8050,
                              23, 11421, 1370, 1369, 16290, 4962, 3298, 787, 274, 2991, 7547, 2025, 8962, 13390, 12134,
                              13176, 3514, 11300, 1573, 8601, 20906, 4097, 18959, 880, 14575, 1965, 7844, 331, 1918,
                              20645, 87, 774, 1974, 1723, 2006, 7702, 4911])

    def test_league_entry(self):
        league_entry = League.LeagueEntry(self.mock_entry)

        self.assertEqual(league_entry.id, 6677)
