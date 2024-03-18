import requests


def top_scorers(league: str, api_token: str):
    url = f'https://api.football-data.org/v4/competitions/{league}/scorers'
    headers = {'X-Auth-Token': api_token}
    params = {'limit': 10}
    scorers = ''

    ans = requests.get(url, headers=headers, params=params).json()

    for i in range(10):
        scorers += (f"{ans['scorers'][i]['player']['name']}: голов - "
                    f"{ans['scorers'][i]['goals']} в {ans['scorers'][i]['playedMatches']} матчах\n")

    return scorers
