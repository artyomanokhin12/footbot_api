from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def start_kb():
    action = ['standings', 'schedule', 'top scorers']

    kb_builder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = [
        KeyboardButton(text=i) for i in action
    ]

    kb_builder.row(*buttons)
    return kb_builder.as_markup(resize_keyboard=True)


def second_kb():
    action = ['premier league', 'la liga', 'serie a']

    kb_builder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = [
        KeyboardButton(text=i) for i in action
    ]

    kb_builder.row(*buttons)

    return kb_builder.as_markup(resize_keyboard=True)

