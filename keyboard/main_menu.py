from aiogram import Bot
from aiogram.types import BotCommand

commands: dict[str, str] = {
    '/standing': 'Текущая турнирная таблица',
    '/schedule': 'Расписание матчей на сегодня',
    '/top_scorers': 'Список лучших бомбардиров чемпионата',
    '/my_team': 'Выбор любимой команды, информация о которой будет приходить в уведомлениях',
    '/change': 'Смена любимой команды',
    '/cancel': 'Отмена действия'
}

async def set_main_menu(bot: Bot) -> None:
    main_menu_commands: list[BotCommand]=[
        BotCommand(command=key, description=value) for key, value in commands.items()
    ]
    await bot.set_my_commands(main_menu_commands)
