from aiogram import Bot

from config.config import load_config

from arq import cron
from arq.connections import RedisSettings

from database.requests import list_users
from other_functions.show_next_match_fav_team import sheduled_match

config = load_config()

host = config.redis_config.host
port = config.redis_config.port
password = config.redis_config.password
db = config.redis_config.db
username = config.redis_config.username

pool_settins = RedisSettings(host=host, port=port, password=password, database=db, username=username)


async def startup(ctx):
    ctx['bot'] = Bot(token=config.tg_bot.token)


async def shutdown(ctx):
    await ctx['bot'].session.close()


async def future_match_notification(ctx):
    _token = config.api_token.token
    bot: Bot = ctx['bot']
    for _ in range(1):
        list_user = await list_users()
        for user in list_user:
            true_user = user[0]
            next_match, matchday = sheduled_match(user[1], _token)
            await bot.send_message(true_user, f"Следующий матч: {next_match}, дата матча: {matchday}")


class WorkerSettings:
    redis_settings = pool_settins
    on_startup = startup
    on_shutdown = shutdown
    functions = [future_match_notification, ]
    cron_jobs = [
        cron('scheduler.scheduler.future_match_notification', second=0)
    ]
    