from database.requests import list_users
from other_functions.show_next_match_fav_team import sheduled_match
from config.config import Config, load_config

config: Config = load_config()

async def weekly_notification(bot):
    _token = config.api_token.token
    for _ in range(1):
        list_user = await list_users()
        for user in list_user:
            true_user = user[0]
            next_match, matchday = sheduled_match(user[1], _token)
            await bot.send_message(true_user, f"Следующий матч: {next_match}, дата матча: {matchday}")
