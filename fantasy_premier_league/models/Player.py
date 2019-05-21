from . import consants


class Player(object):
    def __init__(self, player):
        self.id = player['id']
        self.name = player['web_name']
        self.position = consants.positions[player['element_type']]
        self.ownership = float(player['selected_by_percent'])
        self.photo = player['photo']

    def __str__(self):
        return 'Name: {}, Position: {}, Ownership: {}%'.format(self.name.encode('utf-8'), self.position, self.ownership)
