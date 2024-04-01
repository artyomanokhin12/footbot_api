from datetime import timedelta
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from arq import ArqRedis
from arq.connections import RedisSettings

from database.requests import count_rows, list_users

from config.config import load_config

config = load_config()

router = Router()

pool_settins = RedisSettings(host=config.redis_config.host, port=config.redis_config.port, password=config.redis_config.password, database=config.redis_config.db, username=config.redis_config.username)


@router.message(Command(commands=['count']))
async def command_count(message: Message, arqredis: ArqRedis):
    # result = await count_rows()
    # await message.answer(
    #     text=f"result {result}"
    # )

    await arqredis.enqueue_job()(
        'send_message', _defer_by=timedelta(seconds=5), chat_id=message.from_user.id, text="test"
    )


@router.message(Command(commands=['list']))
async def command_list(message: Message):
    result = await list_users()
    print(result)
    for res in result:
        print(res[0])
    await message.answer(
        text=f"list users: {result}"
    )


@router.message(Command(commands=['redis']))
async def command_redis(message: Message):
    # pool_settins = RedisSettings(host=config.redis_config.host, port=config.redis_config.port, password=config.redis_config.password, database=config.redis_config.db, username=config.redis_config.username)
    print(pool_settins)
    await message.answer(text='команда выполнена')
