from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from keyboard.normal_buttons import second_kb
from state.state import FSMTeamChoice
from other_functions.check_team_id import check_team_id
from keyboard.inline_buttons_fav_team import create_fav_team_keyboard, normal_functions_buttons
from config.config import Config, load_config
from aiogram.types import ReplyKeyboardRemove

from database.requests import test_insert

router = Router()
config: Config = load_config()
api_token = config.api_token.token

# teams_dict: dict[str, str] = {}

league_list = ['PL', 'PD', 'SA']



@router.message(Command(commands=['my_team']), StateFilter(default_state))
async def my_team_command(message: Message, state: FSMContext):
    await message.answer(
        text='Пожалуйста, выбери лигу, в которой находится твоя '
        'любимая команда.',
        reply_markup=normal_functions_buttons()
    )
    await state.set_state(FSMTeamChoice.league)


@router.message(Command(commands=['my_team']), ~StateFilter(default_state))
async def my_team_command_in_state(message: Message):
    await message.answer(
        text='Вы уже находитесь в состоянии выбора.\n\nЕсли хотите '
        'завершить выбор, пожалуйста, введите команду /cancel, или '
        'выберите ее в меню.'
    )


@router.callback_query(StateFilter(FSMTeamChoice.league), F.data.in_(league_list))
async def team_choice(callback: CallbackQuery, state: FSMContext, api_token):
    await state.update_data(league=callback.data)
    team_dict = check_team_id(callback.data, api_token)
    await state.update_data(current_teams=team_dict)
    await callback.message.edit_text(
        text='Пожалуйста, выбери команду, за которой хочешь следить.',
        reply_markup=create_fav_team_keyboard(**team_dict)
    )
    await state.set_state(FSMTeamChoice.team)


@router.callback_query(StateFilter(FSMTeamChoice.league))
async def incorrect_team_choice(callback: CallbackQuery):
    await callback.message.answer(
        text='Пожалуйста, нажмите на одну из кнопок под сообщением.\n'
        'Если вы хотите прекратить выбирать команду, пожалуйста, '
        'введите команду /cancel, или выберите ее в меню.'
    )


@router.callback_query(StateFilter(FSMTeamChoice.team), F.data.in_(FSMContext.get_data(FSMTeamChoice.current_teams)))
async def my_team_final(callback: CallbackQuery, state: FSMContext):
    await state.update_data(team_id=callback.data)
    ans = await state.get_data()
    await callback.message.answer(
        text=f'Вот id команды: {ans['team_id']}'
    )
    await state.clear()






# @router.message(StateFilter(FSMTeamChoice.league), F.text.lower().in_(league_choice))
# async def process_choice_fav_team(message: Message, state: FSMContext):
#     await state.update_data(league=message.text)
#     league = await state.get_data()
#     global teams_dict
#     teams_dict = check_team_id(league_choice[league['league']], api_token=api_token)
#     await message.answer(
#         text="Убираем клавиатуру",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await message.answer(
#         text='Пожалуйста, выберите команду',
#         reply_markup=create_fav_team_keyboard(*teams_dict.keys())
#     )
#     await state.set_state(FSMTeamChoice.team)


# @router.message(StateFilter(FSMTeamChoice.league))
# async def warning_fav_league(message: Message):
#     await message.answer(
#         text='Попробуй еще раз, dumb'
#     )


# @router.callback_query(StateFilter(FSMTeamChoice.team), lambda query: query.data in set(teams_dict.keys()))
# async def process_finale(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(team=callback.data)
#     user_base = await state.get_data()
#     user_base['user_id'] = callback.from_user.id
#     user_base['team_id'] = teams_dict[callback.data]
#     await test_insert(**user_base)

#     await callback.message.answer(
#         text='Отлично! Теперь я могу напоминать тебе о матчах твоей любимой команды!',
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await callback.answer()
#     await state.clear()
#     print(user_base)


# @router.callback_query(StateFilter(FSMTeamChoice.team))
# async def warning_fav_team(callback: CallbackQuery):
#     await callback.message.answer(text='WRONG TEAM:( \n\nTry again')
#     await callback.answer()
