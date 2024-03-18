import requests
from datetime import datetime, date, timedelta
from typing import Awaitable


def schedule(league: str, api_token: str):

    matches = ''

    url = f"http://api.football-data.org/v4/competitions/{league}/matches"
    headers = {"X-Auth-Token": api_token}

    today = date.today()
    monday = today - timedelta(datetime.weekday(today))
    sunday = today + timedelta(6-datetime.weekday(today))

    params = {'dateFrom': today, 'dateTo': today}

    ans = requests.get(url, headers=headers, params=params).json()

    for match in ans['matches']:
        matches += f"{match['homeTeam']['name']} - {match['awayTeam']['name']} ({match['utcDate']})"

    if matches != '':
        return matches
    else:
        matches = 'Сегодня нет матчей'
        return matches
