from aiogram import Bot

from config.config import load_config

from arq import cron
from arq.connections import RedisSettings

from other_functions.weekly_notifications import weekly_notification

from database.requests import list_users
from other_functions.show_next_match_fav_team import sheduled_match

config = load_config()

pool_settins = RedisSettings(host=config.redis_config.host, port=config.redis_config.port, password=config.redis_config.password, database=config.redis_config.db, username=config.redis_config.username)


async def startup(ctx):
    ctx['bot'] = Bot(token=config.tg_bot.token)


async def shutdown(ctx):
    await ctx['bot'].session.close()


async def send_message(ctx, chat_id: int, text: str):
    bot: Bot = ctx['bot']
    await bot.send_message(chat_id, text)


async def plan_message(ctx):
    print('plan')

async def test_notif(ctx):
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
    functions = [send_message, test_notif, ]
    cron_jobs = [
        cron('scheduler.scheduler.test_notif', second=0)
    ]
    