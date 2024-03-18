from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands='test'))
async def command_test(message: Message):
    await message.answer(
        text='Это тестовая функция'
    )
