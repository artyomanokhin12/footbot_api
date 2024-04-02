from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command(commands=['cancel']), StateFilter(default_state))
async def command_cancel_without_state(message: Message):
    await message.answer(
        text='Вы сейчас ничего не выбираете, функция отмены не нужна'
    )


@router.message(Command(commands=['cancel']), ~StateFilter(default_state))
async def command_cancel_with_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы только что вышли из состояния выбора.'
    )
    await state.clear()