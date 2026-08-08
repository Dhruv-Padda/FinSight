from datetime import date, datetime

from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):

    amount: float = Field(gt=0)
    category: str
    description: str| None = None
    date: date

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    description: str|None=None
    date: date
    created_at: datetime
