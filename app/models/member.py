from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

# Avoid circular imports at runtime by using TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.task import Task
    from app.models.activity_log import ActivityLog

class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    capacity: int

    # Relationships
    tasks: List["Task"] = Relationship(back_populates="assignee")
    activity_logs: List["ActivityLog"] = Relationship(back_populates="member")