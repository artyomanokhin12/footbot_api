from dataclasses import dataclass
from typing import Any
from environs import Env
from arq.connections import RedisSettings


@dataclass
class RedisConfig:
    db: int
    host: str
    port: int
    password: str
    username: str
    state_ttl: int
    data_ttl: int


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
    redis_config: RedisConfig


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
        ),
        redis_config=RedisConfig(
            db= 1,
            host='127.0.0.1',
            port= 6379,
            username=None,
            password= None,
            state_ttl=None,
            data_ttl=None
        )
    )
