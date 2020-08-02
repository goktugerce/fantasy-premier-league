urls = {
    'DEFAULT': {
        'BOOTSTRAP_STATIC_URL': 'bootstrap-static',
        'PLAYERS_METADATA_URL': 'elements',
        'ELEMENT_SUMMARY_URL': 'element-summary/',
        'LEAGUE_CLASSIC_STANDINGS_URL': 'leagues-classic/{league_id}/standings/?page_new_entries=1&page_standings={page}&phase=1',
        'TEAM_ENTRY_URL': 'entry/{team_id}/event/{gameweek}/picks',
        'TEAM_HISTORY_URL': 'entry/{team_id}/history'
    },
    'FPL': {
        'BASE_URL': 'https://fantasy.premierleague.com/drf/',
        'KIT_URL': 'https://fantasy.premierleague.com/dist/img/shirts/shirt_{team_id}-110.webp',
        'PORTRAIT_URL': 'https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/110x140/{player_id}.png'
    },
    'ELITESERIEN': {
        'BASE_URL': 'https://fantasy.eliteserien.no/api/',
        'KIT_URL': 'https://en.fantasy.eliteserien.no/dist/img/shirts/standard/shirt_{team_id}-110.png',
        'PORTRAIT_URL': 'https://beta.toppfotball.no/Fantasy/players/{player_id}.png'
    },
    'ALLSVENSKAN': {
        'BASE_URL': 'https://en.fantasy.allsvenskan.se/api/',
        'KIT_URL': 'https://en.fantasy.allsvenskan.se/dist/img/shirts/standard/shirt_{team_id}-110.png',
        'PORTRAIT_URL': 'https://d1y1xe7lamdzn7.cloudfront.net/{player_id}.png'
    }
}
