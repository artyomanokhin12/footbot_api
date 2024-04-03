from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.requests import check_user

router = Router()


@router.message(Command(commands='test'))
async def command_test(message: Message):
    result = await check_user(message.from_user.id)
    await message.answer(f"fav team: {result}")
