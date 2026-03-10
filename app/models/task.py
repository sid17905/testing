from typing import Optional, TYPE_CHECKING
from datetime import date
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.member import Member

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    assignee_id: Optional[int] = Field(default=None, foreign_key="members.id")
    status: str
    progress: int
    due_date: Optional[date] = Field(default=None)

    # Relationship
    assignee: Optional["Member"] = Relationship(back_populates="tasks")