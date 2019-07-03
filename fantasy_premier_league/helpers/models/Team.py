from . import constants


class Team(object):
    def __init__(self, team, **kwargs):
        if team:
            self.id = team['entry_history']['entry']
            self.active_chip = constants.chips[team['active_chip']] if team['active_chip'] else 'No Chip'
            self.picks = []

            for pick in team['picks']:
                self.picks.append(Picks(pick, active_chip=self.active_chip))
        else:
            self.id = kwargs['id']
            self.active_chip = kwargs['active_chip']
            self.picks = []

            for pick in kwargs['picks']:
                self.picks.append(Picks(pick=None, active_chip=None, **pick))


class Picks(object):
    def __init__(self, pick, active_chip, **kwargs):
        if pick:
            self.player_id = pick['element']
            self.position = pick['position']
            self.captain = pick['is_captain']
            self.vice_captain = pick['is_vice_captain']

            if active_chip == 'Bench Boost':
                self.benched = False
            else:
                self.benched = self.position > 11

            self.multiplier = pick['multiplier']
        else:
            self.player_id = kwargs['player_id']
            self.position = kwargs['position']
            self.captain = kwargs['captain']
            self.vice_captain = kwargs['vice_captain']
            self.benched = kwargs['benched']
            self.multiplier = kwargs['multiplier']

    def __eq__(self, other):
        return isinstance(other, self.__class__) and (self.player_id == other.player_id) and (
                    self.position == other.position) and (
                       self.captain == other.captain) and (self.vice_captain == other.vice_captain) and (
                       self.benched == other.benched)
