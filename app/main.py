from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ExpenseCreate
from app.models import Expense


app = FastAPI()

@app.post("/expenses")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):
    db_expense = Expense(user_id = 1,
    amount  = expense.amount,
    category = expense.category,
    description = expense.description,
    date = expense.date)

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense