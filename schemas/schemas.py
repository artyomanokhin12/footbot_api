from pydantic import BaseModel
from datetime import date

class SUser(BaseModel):

    user_id: int
    league: str
    team: str
    team_id: int
    match_notification: bool = None
    date_next_match: date = None
