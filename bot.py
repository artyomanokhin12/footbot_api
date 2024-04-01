import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import RedisStorage, Redis
from arq import create_pool
from config.config import Config, load_config # , RedisConfig
from handlers import action_handlers, fav_team_handlers, for_test
from test import router as test_router, pool_settins
from other_functions.weekly_notifications import weekly_notification

config: Config = load_config()

redis = Redis(host='127.0.0.1')

storage = RedisStorage(redis=redis)

bot = Bot(config.tg_bot.token)
dp = Dispatcher(storage=storage)

dp['api_token'] = config.api_token.token


async def main():

    logging.basicConfig(level=logging.DEBUG)

    redis_pool = await create_pool(pool_settins)

    dp.include_router(fav_team_handlers.router)
    dp.include_router(action_handlers.router)
    dp.include_router(for_test.router)
    dp.include_router(test_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        arqredis=redis_pool
        )


# async def sstart():

#     task1 = asyncio.create_task(main())
#     task2 = asyncio.create_task(weekly_notification(bot=bot))

#     await task1
#     await task2

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот был остановлен")
