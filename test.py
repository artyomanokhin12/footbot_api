from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.requests import count_rows

router = Router()


@router.message(Command(commands=['count']))
async def command_count(message: Message):
    result = await count_rows()
    print("here")
    print(result)
    await message.answer(
        text=f"result"
    )