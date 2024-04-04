from sqlalchemy import Update, func, insert, select, update

from database.user import User
from database.database import async_session_maker
from schemas.schemas import SUser

async def check_user(user_id: int):
    """
    Проверка, есть ли пользователь в БД
    """
    async with async_session_maker() as session:
        print(user_id)
        query = select(User.__table__.columns).filter_by(user_id=user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    

async def favorite_team_insert(**data: SUser):
    async with async_session_maker() as session:
        query = insert(User).values(**data)
        await session.execute(query)
        await session.commit()


async def count_rows():
    async with async_session_maker() as session:
        query = select(func.count()).select_from(User)
        length = await session.scalar(query)
        return length
    

async def list_users():
    async with async_session_maker() as session:
        query = select(User).with_only_columns(User.user_id, User.team_id, User.blocked)
        result = await session.execute(query)
        return result.fetchall()
    

async def block_user(user_id: int, new_status: bool):
    async with async_session_maker() as session:
        query = await session.get(User, user_id)
        query.blocked = new_status
        await session.commit()
