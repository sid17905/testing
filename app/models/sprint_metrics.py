from typing import Optional
from sqlmodel import Field, SQLModel

class SprintMetric(SQLModel, table=True):
    __tablename__ = "sprint_metrics"

    id: Optional[int] = Field(default=None, primary_key=True)
    delay_ratio: float
    blocked_count: int
    avg_workload: float
    sentiment_score: float
    risk_probability: float
    health_score: float