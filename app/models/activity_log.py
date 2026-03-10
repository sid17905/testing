from typing import Optional, TYPE_CHECKING
from datetime import datetime, timezone
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.member import Member

def get_utc_now():
    return datetime.now(timezone.utc)

class ActivityLog(SQLModel, table=True):
    __tablename__ = "activity_logs"

    id: Optional[int] = Field(default=None, primary_key=True)
    member_id: Optional[int] = Field(default=None, foreign_key="members.id")
    message: str
    timestamp: datetime = Field(default_factory=get_utc_now)

    # Relationship
    member: Optional["Member"] = Relationship(back_populates="activity_logs")