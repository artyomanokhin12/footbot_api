from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command, StateFilter
from keyboard.normal_buttons import start_kb, second_kb
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from state.state import FSMLeague

from other_functions import standings, schedule, top_scorers

from typing import Optional, Any


router = Router()


action_dict: dict[str, Optional[Any]] = {
    'standings': standings.test_case,
    'schedule': schedule.schedule,
    'top scorers': top_scorers.top_scorers

}
league_dict: dict[str, str] = {
    'premier league': 'PL',
    'la liga': 'PD',
    'serie a': 'SA'
}


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(
        text='Привет. Выбери действие',
        reply_markup=start_kb()
    )
    await state.set_state(FSMLeague.action)


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text='Ты вне состояния выбора. Тут нечего отменять'
    )


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы только что вышли из выбора действия. '
             'Чтобы еще раз начать действие, введите команду /start'
    )
    await state.clear()


@router.message(StateFilter(FSMLeague.action), F.text.in_(action_dict))
async def standings(message: Message, state: FSMContext):
    await state.update_data(action=message.text)
    await message.answer(text='Выберите лигу', reply_markup=second_kb())
    await state.set_state(FSMLeague.league)


@router.message(StateFilter(FSMLeague.action))
async def warning_action(message: Message):
    await message.answer(
        text='Просто нажми на кнопку, чудик, и ничего не вводи'
    )


@router.message(StateFilter(FSMLeague.league), F.text.in_(league_dict))
async def league_choice(message: Message, state: FSMContext, api_token):
    await state.update_data(league=message.text)
    params = await state.get_data()
    my_func = action_dict[params["action"]]
    await message.answer(
        text=my_func(league_dict[params["league"]], api_token),
        reply_markup=ReplyKeyboardRemove()
    )

    await state.clear()
    

@router.message(StateFilter(FSMLeague.league))
async def warning_league(message: Message):
    await message.answer(
        text='Пожалуйста, нажми на кнопку и выбери лигу. '
             'Если не хочешь - введи команду /cancel'
    )
