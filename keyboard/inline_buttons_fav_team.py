from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

league_dict: dict[str, str] = {
    'premier league': 'PL',
    'la liga': 'PD',
    'serie a': 'SA'
}


def create_fav_team_keyboard(**kwargs: str) -> InlineKeyboardMarkup:
    buttons: list = []
    kb_builder = InlineKeyboardBuilder()
    for name_team, team_id in kwargs.items():
        buttons.append(InlineKeyboardButton(
            text=name_team,
            callback_data=name_team
            ))
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


def normal_functions_buttons() -> InlineKeyboardMarkup:
    buttons: list = []
    kb_builder = InlineKeyboardBuilder()
    for league, league_code in league_dict.items():
        buttons.append(InlineKeyboardButton(
            text=league,
            callback_data=league_code
        ))
    kb_builder.row(*buttons, width=3)
    return kb_builder.as_markup()
