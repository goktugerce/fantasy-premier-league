[![Build Status](https://travis-ci.org/goktugerce/fantasy-premier-league.svg?branch=master)](https://travis-ci.org/goktugerce/fantasy-premier-league)
## Fantasy Premier League variants Stats and Visualization

This project contains a package for collecting captaincy, chip usage, ownership, effective ownership, template team stats from [Fantasy Premier League](https://fantasy.premierleague.com), [Fantasy Allsvenskan](https://en.fantasy.allsvenskan.se), and [Fantasy Eliteserien](http://en.fantasy.eliteserien.no).

## Installation

To be able to run the package, you have to have Python 3+ installed on your computer.

Check if you have python and pip available. If not [you have to install them](https://www.python.org/downloads/).

After running the following command, you are ready to go:

`pip install fantasy-premier-league-stats`

## Usage

First, you have to choose one of the games: `FPL`, `ALLSVENSKAN` or `ELITESERIEN`.

To be able to collect stats and create visualizations, you need to get player information and also the teams. 

```
players = api.get_players(game)
team_ids = api.get_league(league_id, max_players, game)
teams = api.get_league_team_picks(team_ids, gameweek, game)
```

After this, you can get the statistics and plot them if you want (after necessary imports):

```
chip_usage = chips.get_weekly_chip_usage(teams, percentage=True)
captaincy = captains.get_captaincy_stats(teams, players, percentage=True)
ownership_stats = ownership.get_ownership_stats(teams, players)
effective_ownership_stats = ownership.get_effective_ownership_stats(teams, players)
template = template_team.create_template_team(teams, players, effective=True, percentage=True, with_team=True)

plots.draw_chip_usage(chip_usage)
plots.draw_captaincy_stats(captaincy)
plots.draw_ownership_stats(ownership_stats)
plots.draw_effective_ownership_stats(effective_ownership_stats)
plots.draw_template_team(template, game)
```

You can either see the plots while running your script or save them to a path of your choice.

Another point is that team picks are cached in path `~/.fpl` folder, and if you do not want to download team picks again, you can add `overwrite=False` to `api.get_league_team_picks` function call. If you want to clear the directory, you can run `clear_directory` function in `utilities`.

## Future Improvements and Contributing

I do not plan to enhance the package into containing live stats, but all contributions are welcome. You can create issues for feature requests and bugs. You can also contribute by adding features and creating pull requests.
