urls = {
    'DEFAULT': {
        'BOOTSTRAP_STATIC_URL': 'bootstrap-static',
        'PLAYERS_METADATA_URL': 'elements',
        'ELEMENT_SUMMARY_URL': 'element-summary/',
        'LEAGUE_CLASSIC_STANDINGS_URL': 'leagues-classic-standings/{league_id}?phase=1&le-page=1&ls-page={page}',
        'TEAM_ENTRY_URL': 'entry/{team_id}/event/{gameweek}/picks',
    },
    'FPL': {
        'BASE_URL': 'https://fantasy.premierleague.com/drf/',
        'KIT_URL': 'https://fantasy.premierleague.com/dist/img/shirts/shirt_{team_id}-110.webp',
        'PORTRAIT_URL': 'https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/110x140/{player_id}.png'
    },
    'ELITESERIEN': {
        'BASE_URL': 'https://fantasy.eliteserien.no/drf/',
        'KIT_URL': 'https://en.fantasy.eliteserien.no/static/libsass/eliteserienf/dist/img/shirts/shirt_{team_id}-300.png',
        'PORTRAIT_URL': 'https://beta.toppfotball.no/Fantasy/players/{player_id}.png'
    },
    'ALLSVENSKAN': {
        'BASE_URL': 'https://en.fantasy.allsvenskan.se/drf/',
        'KIT_URL': 'https://en.fantasy.allsvenskan.se/static/libsass/allsvenskanf/dist/img/shirts/shirt_{team_id}-300.png',
        'PORTRAIT_URL': 'https://d1y1xe7lamdzn7.cloudfront.net/{player_id}.png'
    }
}
