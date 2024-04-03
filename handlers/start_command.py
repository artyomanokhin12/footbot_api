from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text="Привет! Ты только что запустил футбольного бота-информатора.\n\n"
        "Здесь ты можешь посмотреть актуальную информацию по топ-5 лигам мира: текущее положение команд,"
        "расписание ближайших матчей и лучших бомбардиров на данный момент.\n\n"
        "Все команды доступны в меню. Если хочешь, можешь ввести команду /help или выбрать ее в меню, "
        "чтобы узнать о возможностях бота более подробно."
    )


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(
        text='Пока что дополнительной информации нет'
    )
    