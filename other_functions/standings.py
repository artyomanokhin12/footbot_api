import requests


def standing(league, api_token):

    url = f"http://api.football-data.org/v4/competitions/{league}/standings"
    headers = {"X-Auth-Token": api_token}
    params = {"season": 2023}
    result = requests.get(url, headers=headers, params=params).json()
    len_res = len(result["standings"][0]["table"])
    standing = ''
    for i in range(len_res):
        standing += (f"{1 + i}) {result["standings"][0]["table"][i]["team"]["name"]} - {result["standings"][0]["table"][i]["points"]} очков "
        f"за {result["standings"][0]["table"][i]["playedGames"]} игр\n")
    return standing

