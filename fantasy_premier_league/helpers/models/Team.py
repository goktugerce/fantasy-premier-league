from . import constants


class Team(object):
    def __init__(self, team, **kwargs):
        if team:
            self.id = team['entry_history']['entry']
            self.active_chip = constants.chips[team['active_chip']] if team['active_chip'] else ''
            self.picks = []

            for pick in team['picks']:
                self.picks.append(Picks(pick))
        else:
            self.id = kwargs['id']
            self.active_chip = kwargs['active_chip']
            self.picks = []

            for pick in kwargs['picks']:
                self.picks.append(Picks(pick=None, **pick))


class Picks(object):
    def __init__(self, pick, **kwargs):
        if pick:
            self.player_id = pick['element']
            self.position = pick['position']
            self.captain = pick['is_captain']
            self.vice_captain = pick['is_vice_captain']
            self.multiplier = pick['multiplier']
        else:
            self.player_id = kwargs['player_id']
            self.position = kwargs['position']
            self.captain = kwargs['captain']
            self.vice_captain = kwargs['vice_captain']
            self.multiplier = kwargs['multiplier']
