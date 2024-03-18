import requests
from config.config import Config, load_config

config = load_config()

headers = {'X-Auth-Token': config.api_token.token}
print("IN FUNC")

url = f'https://api.football-data.org/v4/teams/{64}/matches?status=SCHEDULED'
ans = requests.get(url=url, headers=headers).json()
print(ans)
matchday = ans['matches'][0]['utcDate']
next_match = ans['matches'][0]['homeTeam']['name'] + " " + ans['matches'][0]['awayTeam']['name']
print(next_match, matchday)
