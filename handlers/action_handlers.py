from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from state.state import FSMLeague

from other_functions.standings import standing
from other_functions.schedule import schedule
from other_functions.top_scorers import top_scorers
from keyboard.normal_buttons import second_kb
from keyboard.inline_buttons_fav_team import normal_functions_buttons

router = Router()


action_dict = {
    'standing': standing,
    'schedule': schedule,
    'top_scorers': top_scorers
}

league_list = ['PL', 'PD', 'SA']


@router.message(Command(commands=['standing', 'schedule', 'top_scorers']), StateFilter(default_state))
async def standing_command(message: Message, state: FSMContext) -> None:
    await state.update_data(action=(message.text).replace('/', ''))
    await message.answer(
        text='Выбери лигу, чью турнирную таблицу хочешь посмотреть',
        reply_markup=normal_functions_buttons()
    )
    await state.set_state(FSMLeague.league)


@router.message(Command(commands=['standing', 'schedule', 'top_scorers']), ~StateFilter(default_state))
async def standing_command_in_state(message: Message):
    await message.answer(
        text='Вы уже находитесь в состоянии выбора. Если вы '
        'хотите отменить действие, введите команду /cancel'
    )


@router.callback_query(StateFilter(FSMLeague.league), F.data.in_(league_list))
async def league_choice(callback: CallbackQuery, state: FSMContext, api_token) -> None:
    await state.update_data(league=callback.data)
    params = await state.get_data()
    await callback.answer('Идет загрузка')
    await callback.message.answer(
        text=action_dict[params['action']](params['league'], api_token)
    )
    await callback.message.delete()
    await state.clear()


@router.message(StateFilter(FSMLeague.league))
async def warning_league(message: Message):
    await message.answer(
        text="Пожалуйста, нажмите на кнопку выбора лиги.\n"
            "Если вы хотите прервать выполнение текущего запроса, "
            "введите команду /cancel, или выберите ее в меню."
    )
