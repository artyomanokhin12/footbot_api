import requests
from datetime import datetime, date, timedelta

from other_functions.my_timezone import timezone_change


def schedule(league: str, api_token: str):

    matches = ''

    url = f"http://api.football-data.org/v4/competitions/{league}/matches"
    headers = {"X-Auth-Token": api_token}

    today = date.today()

    params = {'dateFrom': today, 'dateTo': today}

    ans = requests.get(url, headers=headers, params=params).json()

    for match in ans['matches']:
        matchday = match['utcDate']
        matchday_msk = timezone_change(matchday)
        matches += f"{match['homeTeam']['name']} - {match['awayTeam']['name']}. {matchday_msk}\n"

    if matches:
        return matches
    else:
        return 'Сегодня нет матчей'
