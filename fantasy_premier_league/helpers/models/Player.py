from . import constants


class Player(object):
    def __init__(self, player, game):
        self.id = player['id']
        self.code = player['code']
        self.name = player['web_name']
        self.team = constants.teams[game][player['team_code']]
        self.team_id = player['team_code']
        self.position = constants.positions[player['element_type']]
        self.ownership = float(player['selected_by_percent'])
        self.photo = player['photo']

    def __str__(self):
        return 'Name: {}, Position: {}, Ownership: {}%'.format(self.name.encode('utf-8'), self.position, self.ownership)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and (self.id == other.id) and (self.code == other.code)
