from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from state.state import FSMTeamChoice
from other_functions.check_team_id import check_team_id
from keyboard.inline_buttons_fav_team import create_fav_team_keyboard, normal_functions_buttons
from config.config import Config, load_config

from database.requests import favorite_team_insert

router = Router()
config: Config = load_config()
api_token = config.api_token.token

league_list = ['PL', 'PD', 'SA']



@router.message(Command(commands=['my_team']), StateFilter(default_state))
async def my_team_command(message: Message, state: FSMContext) -> None:
    await message.answer(
        text='Пожалуйста, выбери лигу, в которой находится твоя '
        'любимая команда.',
        reply_markup=normal_functions_buttons()
    )
    await state.set_state(FSMTeamChoice.league)


@router.message(Command(commands=['my_team']), ~StateFilter(default_state))
async def my_team_command_in_state(message: Message) -> None:
    await message.answer(
        text='Вы уже находитесь в состоянии выбора.\n\nЕсли хотите '
        'завершить выбор, пожалуйста, введите команду /cancel, или '
        'выберите ее в меню.'
    )


@router.callback_query(StateFilter(FSMTeamChoice.league), F.data.in_(league_list))
async def team_choice(callback: CallbackQuery, state: FSMContext, api_token) -> None:
    await callback.answer('Идет загрузка')
    await state.update_data(league=callback.data)
    team_dict = check_team_id(callback.data, api_token)
    await state.update_data(current_teams=team_dict)
    await callback.message.edit_text(
        text='Пожалуйста, выбери команду, за которой хочешь следить.',
        reply_markup=create_fav_team_keyboard(**team_dict)
    )
    await state.set_state(FSMTeamChoice.team)


@router.callback_query(StateFilter(FSMTeamChoice.league))
async def incorrect_team_choice(callback: CallbackQuery) -> None:
    await callback.message.answer(
        text='Пожалуйста, нажмите на одну из кнопок под сообщением.\n'
        'Если вы хотите прекратить выбирать команду, пожалуйста, '
        'введите команду /cancel, или выберите ее в меню.'
    )


@router.callback_query(StateFilter(FSMTeamChoice.team))
async def vivod(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(team=callback.data)
    data = await state.get_data()
    if callback.data not in data['current_teams'].keys():
        await callback.message.edit_text(
            text='Пожалуйста, выберите команду, нажав на кнопку с названием.\n\n'
            'Если вы хотите прекратить выбирать команду, пожалуйста, введите' 
            'команду /cancel, или выберите ее в меню.'
        )
    else:
        await callback.answer('Идет загрузка')
        await callback.message.answer(
            text='Отлично, теперь я могу напоминать вам о предстоящих матчах вашей команды!'
        )
        await callback.message.delete()
        print(data)
        data['user_id'] = callback.from_user.id
        data['team_id'] = data['current_teams'][data['team']]
        data['blocked'] = False
        data.pop('current_teams', None)
        print(data)
        await favorite_team_insert(**data)
        await state.clear()
