import requests
from other_functions.my_timezone import timezone_change


def sheduled_match(team_id: str, api_token: str):
    print("IN FUNC")
    headers = {"X-Auth-Token": api_token}
    url = f'https://api.football-data.org/v4/teams/{team_id}/matches?status=SCHEDULED'
    ans = requests.get(url=url, headers=headers).json()
    matchday = ans['matches'][0]['utcDate']
    matchday_msk = timezone_change(matchday)
    next_match = ans['matches'][0]['homeTeam']['name'] + " " + ans['matches'][0]['awayTeam']['name']
    return next_match, matchday_msk
