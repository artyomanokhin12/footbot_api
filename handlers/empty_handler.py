from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def empty_message(message: Message):
    await message.answer(
        text='Не могу распознать команду. Пожалуйста, введите команду /help '
        'или выберите ее в меню, чтобы посмотреть мои возможности.'
    )
    