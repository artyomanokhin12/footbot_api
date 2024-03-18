import asyncio

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import for_test

config: Config = load_config()
bot = Bot(token=config.tg_bot.token)
# dp = Dispatcher()
# dp.include_router(for_test.router)
# bot.delete_webhook(drop_pending_updates=True)


async def main():
    # while True:

    dp = Dispatcher()
    dp.include_router(for_test.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def timer():
    while True:
        await asyncio.sleep(5)
        await bot.send_message(chat_id=392039047, text='Это тестовая функция с таймером')


async def gigamain():

    loop = asyncio.get_event_loop()
    await loop.create_task(timer())
    await main()



if __name__ == '__main__':
    asyncio.run(gigamain())



# 392039047

#
# if __name__ == "__main__":
#     dp.run_polling(bot)
