from aiogram.fsm.state import StatesGroup, State


class FSMLeague(StatesGroup):
    action = State()
    league = State()


class FSMTeamChoice(StatesGroup):
    league = State()
    current_teams = State()
    team = State()
