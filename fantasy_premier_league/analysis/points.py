from collections import defaultdict
from . import helpers

def get_current_ranks(teams):
  """Get current ranks of teams"""
  current_ranks = defaultdict(int)
  for team in teams:
    last_week = team.current_season[-1]
    current_ranks[team.id] = last_week['overall_rank']
  
  return sorted(current_ranks.items(), key = lambda item: item[1])


def get_hall_of_fame(teams, cutoff_past):
  best_teams = defaultdict(list)
  for team in teams:
    for season in team.past:
      if season['rank'] <= cutoff_past:
        best_teams[team.id].append(season['rank'])
  
  sorted_teams = sorted(best_teams.items(), key= lambda item: len(item[1]), reverse=True)
  
  return sorted_teams