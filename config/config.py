from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class ApiToken:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    api_token: ApiToken


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN")
        ),
        api_token=ApiToken(
            token=env("API_TOKEN")
        )
    )
