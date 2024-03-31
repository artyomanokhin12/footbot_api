import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import RedisStorage, Redis
from config.config import Config, load_config
from handlers import action_handlers, fav_team_handlers, for_test
from other_functions.show_next_match_fav_team import sheduled_match
from database.database import user_base

config: Config = load_config()

redis = Redis(host='127.0.0.1')

storage = RedisStorage(redis=redis)

bot = Bot(config.tg_bot.token)
dp = Dispatcher(storage=storage)

dp['api_token'] = config.api_token.token


async def main():

    logging.basicConfig(level=logging.DEBUG)

    dp.include_router(fav_team_handlers.router)
    dp.include_router(action_handlers.router)
    dp.include_router(for_test.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def weekly_notification():
    while True:
        await asyncio.sleep(60)
        cur_date = datetime.isoweekday(datetime.now())

        if cur_date == 6 and user_base:
            for user_id in user_base.items():
                next_match, matchday = sheduled_match(
                    user_base[user_id]['team_id'],
                    api_token=config.api_token.token)
                await bot.send_message(user_id,
                                       f'Следующий матч: {next_match},'
                                       f'дата матча: {matchday}')


async def sstart():

    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(weekly_notification())

    await task1
    await task2

if __name__ == "__main__":
    try:
        asyncio.run(sstart())
    except (KeyboardInterrupt, SystemExit):
        print("Бот был остановлен")
