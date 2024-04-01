from datetime import timedelta
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from arq import ArqRedis

from database.requests import count_rows, list_users

router = Router()


@router.message(Command(commands=['count']))
async def command_count(message: Message, arqredis: ArqRedis):
    result = await count_rows()
    await message.answer(
        text=f"result {result}"
    )

    await arqredis.enqueue_job(
        'weekly_notification', _defer_by=timedelta(second=10), chat_id=message.from_user.id, text="test"
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
