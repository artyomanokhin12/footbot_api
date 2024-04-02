import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import RedisStorage, Redis
from config.config import Config, load_config
from handlers import action_handlers, fav_team_handlers, for_test
from test import router as test_router


async def main():    

    logging.basicConfig(level=logging.DEBUG)
    
    bot = Bot(config.tg_bot.token)
    
    dp['api_token'] = config.api_token.token

    config: Config = load_config()

    redis = Redis(host='127.0.0.1')

    storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)
    
    dp.include_router(fav_team_handlers.router)
    dp.include_router(action_handlers.router)
    dp.include_router(for_test.router)
    dp.include_router(test_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот был остановлен")
