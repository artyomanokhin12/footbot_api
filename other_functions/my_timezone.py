from datetime import datetime, timedelta
# print((datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("Date: %Y %m %d, time: %H:%M "))

def timezone_change(matchday):
    matchday = datetime.strptime(matchday, "%Y-%m-%dT%H:%M:%SZ")
    matchday_msk = matchday + timedelta(hours=3)
    return matchday_msk.strftime("Дата матча: %d.%m.%Y, время: %H:%M ")