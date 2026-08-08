from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ExpenseCreate, ExpenseResponse
from app.models import Expense


app = FastAPI()

@app.post("/expenses", response_model=ExpenseResponse)
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

@app.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def return_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if expense is None:
        raise HTTPException(
            status_code = 404,
            detail="Expense not found"
        )

    return expense