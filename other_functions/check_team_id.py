import requests


def check_team_id(league: str, api_token: str):
    url = f"http://api.football-data.org/v4/competitions/{league}/teams"
    headers: dict[str, str] = {"X-Auth-Token": api_token}
    ans = requests.get(url=url, headers=headers).json()
    teams_id: dict[int, str] = {}
    for i in range(len(ans['teams'])):
        teams_id[ans['teams'][i]['name']] = ans['teams'][i]['id']
    return teams_id
