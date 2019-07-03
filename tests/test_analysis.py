from unittest import TestCase
from collections import OrderedDict

from .files.mocks import *
from fantasy_premier_league.helpers.models import Team, Player
from fantasy_premier_league.analysis import *
from fantasy_premier_league.api import get_players


class TestAnalysis(TestCase):
    def setUp(self):
        self.team_entries = mock_teams_data
        self.teams = [Team.Team(team=None, **team) for team in self.team_entries]
        self.players = get_players('ALLSVENSKAN')

    def test_weekly_chip_usage(self):
        chip_usage = chips.get_weekly_chip_usage(self.teams)

        expected_chip_usage = OrderedDict()
        expected_chip_usage['Park the Bus'] = 0.8
        expected_chip_usage['Attack! Attack!'] = 0.2

        for actual, expected in zip(chip_usage.items(), expected_chip_usage.items()):
            self.assertEqual(actual, expected)

    def test_captaincy(self):
        captaincy = captains.get_captaincy_stats(self.teams, self.players, percentage=True)

        expected_captaincy = OrderedDict()
        expected_captaincy['Larsson (NOR)'] = 0.6
        expected_captaincy['Witry (DIF)'] = 0.2
        expected_captaincy['Ring (DIF)'] = 0.2

        for actual, expected in zip(captaincy.items(), expected_captaincy.items()):
            self.assertEqual(actual, expected)

    def test_ownership(self):
        actual_ownership = ownership.get_ownership_stats(self.teams, self.players)

        expected_ownership = OrderedDict()
        expected_ownership['Witry (DIF)'] = 1.0
        expected_ownership['Larsson (NOR)'] = 1.0
        expected_ownership['Jarl (AFC)'] = 1.0
        expected_ownership['Larsen (NOR)'] = 0.8
        expected_ownership['Elyounoussi (AIK)'] = 0.8
        expected_ownership['Tankovic (HAM)'] = 0.8
        expected_ownership['Joelsson (HIF)'] = 0.6
        expected_ownership['Ring (DIF)'] = 0.6
        expected_ownership['Sundgren (AIK)'] = 0.6
        expected_ownership['Krogh Gerson (NOR)'] = 0.6
        expected_ownership['Rieks (MFF)'] = 0.6
        expected_ownership['Karlsson (AIK)'] = 0.4
        expected_ownership['Mets (AIK)'] = 0.4
        expected_ownership['Christiansen (MFF)'] = 0.4
        expected_ownership['Dimitriadis (AIK)'] = 0.4
        expected_ownership['Jeremejeff (BKH)'] = 0.4
        expected_ownership['Yusuf (GBG)'] = 0.4
        expected_ownership['Dahlin (MFF)'] = 0.4
        expected_ownership['Dagerstål (NOR)'] = 0.2
        expected_ownership['Batanero (SUN)'] = 0.2
        expected_ownership['Bråtveit (DIF)'] = 0.2
        expected_ownership['Sylisufaj (FFF)'] = 0.2
        expected_ownership['Linnér (AIK)'] = 0.2
        expected_ownership['Sema (SUN)'] = 0.2
        expected_ownership['Hägg Johansson (KFF)'] = 0.2
        expected_ownership['Karlsson-Lagemyr (GBG)'] = 0.2
        expected_ownership['Kharaishvili (GBG)'] = 0.2
        expected_ownership['Ulvestad (DIF)'] = 0.2
        expected_ownership['Traustason (MFF)'] = 0.2
        expected_ownership['Buya Turay (DIF)'] = 0.2
        expected_ownership['Pettersson (NOR)'] = 0.2
        expected_ownership['Danielsson (DIF)'] = 0.2
        expected_ownership['Larsson (AIK)'] = 0.2
        expected_ownership['Brattberg (FFF)'] = 0.2
        expected_ownership['Berg (DIF)'] = 0.2
        expected_ownership['Sandberg (HAM)'] = 0.2
        expected_ownership['Åstedt (AFC)'] = 0.2

        for actual, expected in zip(actual_ownership.items(), expected_ownership.items()):
            self.assertEqual(actual, expected)

    def test_effective_ownership(self):
        actual_effective_ownership = ownership.get_effective_ownership_stats(self.teams, self.players)

        expected_effective_ownership = OrderedDict()
        expected_effective_ownership['Witry (DIF)'] = 1.8
        expected_effective_ownership['Larsen (NOR)'] = 1.6
        expected_effective_ownership['Larsson (NOR)'] = 1.2
        expected_effective_ownership['Krogh Gerson (NOR)'] = 1.2
        expected_effective_ownership['Elyounoussi (AIK)'] = 1.0
        expected_effective_ownership['Sundgren (AIK)'] = 1.0
        expected_effective_ownership['Karlsson (AIK)'] = 0.8
        expected_effective_ownership['Mets (AIK)'] = 0.8
        expected_effective_ownership['Dimitriadis (AIK)'] = 0.8
        expected_effective_ownership['Ring (DIF)'] = 0.6
        expected_effective_ownership['Rieks (MFF)'] = 0.6
        expected_effective_ownership['Jeremejeff (BKH)'] = 0.6
        expected_effective_ownership['Joelsson (HIF)'] = 0.4
        expected_effective_ownership['Dagerstål (NOR)'] = 0.4
        expected_effective_ownership['Christiansen (MFF)'] = 0.4
        expected_effective_ownership['Batanero (SUN)'] = 0.2
        expected_effective_ownership['Tankovic (HAM)'] = 0.2
        expected_effective_ownership['Jarl (AFC)'] = 0.2
        expected_effective_ownership['Linnér (AIK)'] = 0.2
        expected_effective_ownership['Sema (SUN)'] = 0.2
        expected_effective_ownership['Kharaishvili (GBG)'] = 0.2
        expected_effective_ownership['Dahlin (MFF)'] = 0.2
        expected_effective_ownership['Traustason (MFF)'] = 0.2
        expected_effective_ownership['Buya Turay (DIF)'] = 0.2
        expected_effective_ownership['Pettersson (NOR)'] = 0.2
        expected_effective_ownership['Danielsson (DIF)'] = 0.2
        expected_effective_ownership['Larsson (AIK)'] = 0.2
        expected_effective_ownership['Bråtveit (DIF)'] = 0.0
        expected_effective_ownership['Sylisufaj (FFF)'] = 0.0
        expected_effective_ownership['Hägg Johansson (KFF)'] = 0.0
        expected_effective_ownership['Karlsson-Lagemyr (GBG)'] = 0.0
        expected_effective_ownership['Yusuf (GBG)'] = 0.0
        expected_effective_ownership['Ulvestad (DIF)'] = 0.0
        expected_effective_ownership['Brattberg (FFF)'] = 0.0
        expected_effective_ownership['Berg (DIF)'] = 0.0
        expected_effective_ownership['Sandberg (HAM)'] = 0.0
        expected_effective_ownership['Åstedt (AFC)'] = 0.0

        for actual, expected in zip(actual_effective_ownership.items(), expected_effective_ownership.items()):
            self.assertEqual(actual, expected)

    def test_template_team(self):
        actual_template_team = template_team.create_template_team(self.teams, self.players, effective=True,
                                                                  percentage=True, with_team=True)

        expected_template_team = {'GK': [helpers.find_player_by_id(self.players, 9),
                                         helpers.find_player_by_id(self.players, 386)],
                                  'DEF': [helpers.find_player_by_id(self.players, 211),
                                          helpers.find_player_by_id(self.players, 291),
                                          helpers.find_player_by_id(self.players, 272),
                                          helpers.find_player_by_id(self.players, 387),
                                          helpers.find_player_by_id(self.players, 379)],
                                  'MID': [helpers.find_player_by_id(self.players, 203),
                                          helpers.find_player_by_id(self.players, 24),
                                          helpers.find_player_by_id(self.players, 43),
                                          helpers.find_player_by_id(self.players, 370),
                                          helpers.find_player_by_id(self.players, 60)],
                                  'FWD': [helpers.find_player_by_id(self.players, 283),
                                          helpers.find_player_by_id(self.players, 380),
                                          helpers.find_player_by_id(self.players, 183)]}

        self.assertDictEqual(actual_template_team, expected_template_team)
