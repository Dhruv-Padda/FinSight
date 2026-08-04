from datetime import date
from pydantic import BaseModel

class ExpenseCreate(BaseModel):

    amount: float
    category: str
    description: str| None = None
    date: date

