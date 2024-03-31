from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class ApiToken:
    token: str


@dataclass
class Database:
    driver: str
    database_name: str
    username: str
    port: str
    host: str
    password: str

    
@dataclass
class Config:
    tg_bot: TgBot
    api_token: ApiToken
    database: Database


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN")
        ),
        api_token=ApiToken(
            token=env("API_TOKEN")
        ),
        database=Database(
            driver=env('driver'),
            database_name=env('database_name'),
            username=env('username'),
            port=env('port'),
            host=env('host'),
            password=env('password')
        )
    )
