from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    league = Column(VARCHAR(30), unique=False, nullable=False)
    team = Column(VARCHAR(40), unique=False, nullable=False)
    team_id = Column(Integer, unique=False, nullable=False)
    match_notification = Column(Boolean, unique=False, nullable=False)
    date_next_match = Column(DATE)

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"
