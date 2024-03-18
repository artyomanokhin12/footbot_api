import requests


def sheduled_match(team_id: str, api_token: str):
    print("IN FUNC")
    headers = {"X-Auth-Token": api_token}
    url = f'https://api.football-data.org/v4/teams/{team_id}/matches?status=SCHEDULED'
    ans = requests.get(url=url, headers=headers).json()
    matchday = ans['matches'][0]['utcDate']
    next_match = ans['matches'][0]['homeTeam']['name'] + " " + ans['matches'][0]['awayTeam']['name']
    return next_match, matchday
