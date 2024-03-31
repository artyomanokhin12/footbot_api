from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.requests import test_request, test_insert
from database.database import async_session_maker

router = Router()


@router.message(Command(commands='test'))
async def command_test(message: Message):
    result = await test_request(message.from_user.id)
    await message.answer(f"fav team: {result}")
