class LeagueStandings(object):
    def __init__(self, league):
        self.name = league['league']['name']
        self.id = league['league']['id']
        self.teams = []

        for team in league['standings']['results']:
            self.teams.append(LeagueEntry(team))

    def get_team_ids(self):
        return [team.id for team in self.teams]


class LeagueEntry(object):
    def __init__(self, entry):
        self.id = entry['entry']
