import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import RedisStorage, Redis
from config.config import Config, load_config
from handlers import action_handlers, fav_team_handlers, for_test
from other_functions.show_next_match_fav_team import sheduled_match
from database.database import user_base
from test import router as test_router
from other_functions.weekly_notifications import weekly_notification

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
    dp.include_router(test_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def sstart():

    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(weekly_notification(bot=bot))

    await task1
    await task2

if __name__ == "__main__":
    try:
        asyncio.run(sstart())
    except (KeyboardInterrupt, SystemExit):
        print("Бот был остановлен")
