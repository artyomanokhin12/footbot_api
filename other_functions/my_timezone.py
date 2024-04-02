from datetime import datetime, timedelta
# print((datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("Date: %Y %m %d, time: %H:%M "))

def timezone_change(matchday, fav_team: bool = None):
    matchday = datetime.strptime(matchday, "%Y-%m-%dT%H:%M:%SZ")
    matchday_msk = matchday + timedelta(hours=3)
    if fav_team:
        cur_date = datetime.now()
        delta = abs((matchday_msk - cur_date).days)
        if delta:
            matchday_msk = None
            return matchday_msk 
    return matchday_msk.strftime("Дата матча: %d.%m.%Y, время: %H:%M ")