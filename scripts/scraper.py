import requests
from time import sleep
import pandas as pd


def get_round_fixture_ids(tournament_id, season_id, round_id):
    url = f'https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}/' + \
          f'season/{season_id}/events/round/{round_id}'
    r = requests.get(url)
    json = r.json()
    event_ids = [e['id'] for e in json['events']]
    return event_ids


def get_teams(fixture_id):
    url = f'https://api.sofascore.com/api/v1/event/{fixture_id}'
    r = requests.get(url)
    json = r.json()
    home_team = json['event']['homeTeam']
    away_team = json['event']['awayTeam']
    return {'home': home_team, 'away': away_team}


def get_statistics(fixture_id, teams):
    url = f'https://api.sofascore.com/api/v1/event/{fixture_id}/lineups'
    r = requests.get(url)
    json = r.json()
    all_stats = []
    for t in ['home', 'away']:
        team = teams[t]
        for player in json[t]['players']:
            player_stats = {}
            if player['position'] == 'G':
                continue
            player_stats['id'] = player['player']['id']
            player_stats['name'] = player['player']['name']
            player_stats['team'] = team['name']
            player_stats['position'] = player['position']
            player_stats['minutesPlayed'] = player['statistics'].get('minutesPlayed', 0)

            if player_stats['minutesPlayed'] == 0:
                continue

            player_stats['goals'] = player['statistics'].get('goals', 0)

            player_stats['goalAttempts'] = player['statistics'].get('onTargetScoringAttempt', 0) + \
                                           player['statistics'].get('blockedScoringAttempt', 0) + \
                                           player['statistics'].get('shotOffTarget', 0)

            for stat in ['onTargetScoringAttempt', 'savedShotsFromInsideTheBox', 'bigChanceMissed', 'goalAssist',
                         'keyPass',
                         'bigChanceCreated', 'touches', 'totalCross', 'accurateCross']:
                player_stats[stat] = player['statistics'].get(stat, 0)

            all_stats.append(player_stats)
    return all_stats


all_stats = []

for week in range(6, 12):
    fixture_ids = get_round_fixture_ids(20, 26799, week)
    for fixture_id in fixture_ids:
        teams = get_teams(fixture_id)
        player_stats = get_statistics(fixture_id, teams)
        all_stats += player_stats
        print(week, fixture_id)
        sleep(1)

print(len(all_stats))
pd.DataFrame(all_stats).to_csv('data/raw.csv', index=False)

# r = requests.get('https://api.sofascore.com/api/v1/unique-tournament/20/season/26799/events/round/10')
# print(r.json())
