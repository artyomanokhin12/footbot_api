from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.requests import count_rows, list_users

router = Router()


@router.message(Command(commands=['count']))
async def command_count(message: Message):
    result = await count_rows()
    await message.answer(
        text=f"result {result}"
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
