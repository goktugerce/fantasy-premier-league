from ..utilities import get_kit_url, get_portrait_url


def prepare_data(dictionary, key_name, value_name, limit=10):
    """Prepare data for the bar plot. Convert key, value pairs to named objects"""
    data = []
    for key, value in dictionary.items():
        record = {key_name: key, value_name: value}
        data.append(record)
    return data[:limit]


def prepare_template_team_data(template_team):
    """Prepare template team data with each player in necessary subplot positions."""

    # GK starts from 1 because there is only two goalies, FWD starts from 16 because there are only three forwards
    position_offsets = {'GK': 1, 'DEF': 5, 'MID': 10, 'FWD': 16}

    data = []
    for position, players in template_team.items():
        for idx, player in enumerate(players):
            data.append({
                'code': player.code,
                # One empty spot between two goalkeepers
                'idx': position_offsets[position] + (idx if position != 'GK' else 2 * idx),
                'team': player.team_id,
                'label': f'{player.name} ({player.ownership}%)'
            })
    return data


def prepare_images(data, game='FPL'):
    """Download images from the URLs. If a player portrait does not exist, download the team photo"""
    import requests
    from PIL import Image
    from io import BytesIO

    images = []
    for p in data:
        try:
            images.append({'image': Image.open(BytesIO(requests.get(get_portrait_url(p['code'], game)).content)),
                           'index': p['idx']})
        except OSError:
            # When the image is nonexistent, BytesIO will throw an OSError
            try:
                images.append({'image': Image.open(BytesIO(requests.get(get_kit_url(p['team'], game)).content)),
                               'index': p['idx']})
            except requests.exceptions.SSLError:
                # Allsvenskan does not work with secure requests for some reason at the moment
                images.append(
                    {'image': Image.open(BytesIO(requests.get(get_kit_url(p['team'], game), verify=False).content)),
                     'index': p['idx']})
    return images
