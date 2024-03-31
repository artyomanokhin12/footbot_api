from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean, String, Date

from database.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=False)
    league = Column(String, unique=False, nullable=False)
    team = Column(String, unique=False, nullable=False)
    team_id = Column(Integer, unique=False, nullable=False)
    match_notification = Column(Boolean, unique=False, nullable=True)
    date_next_match = Column(Date, unique=False, nullable=True)

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"
