# from aiogram import Bot
# from aiogram.methods import send_message

# from config.config import load_config, RedisConfig

# config = load_config()


# async def startup(ctx):
#     ctx['bot'] = Bot(token=config.tg_bot.token)


# async def shutdown(ctx):
#     await ctx['bot'].session.close()


# async def weekly_notification(ctx, chat_id: int, text: str):
#     bot: Bot = ctx['bot']
#     await bot.send_message(chat_id, text)


# class WorkerSettings:
#     redis_settings = RedisConfig.pool_settings
#     on_startup = startup
#     on_shutdown = shutdown
#     functions = [send_message, ]
    