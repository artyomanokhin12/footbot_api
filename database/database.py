user_base = {}

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config.config import Config, load_config

config: Config = load_config()

driver = config.database.driver
database_name = config.database.database_name
username = config.database.username
port = config.database.port
host = config.database.host
password = config.database.password

DATABASE_URL = f"{driver}://{username}:{password}@{host}:{port}/{database_name}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
