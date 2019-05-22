from . import constants


class Team(object):
    def __init__(self, team):
        self.id = team['entry_history']['entry']
        self.active_chip = constants.chips[team['active_chip']] if team['active_chip'] else ''
        self.picks = []

        for pick in team['picks']:
            self.picks.append(Picks(pick))


class Picks(object):
    def __init__(self, pick):
        self.player_id = pick['element']
        self.position = pick['position']
        self.captain = pick['is_captain']
        self.vice_captain = pick['is_vice_captain']
        self.multiplier = pick['multiplier']