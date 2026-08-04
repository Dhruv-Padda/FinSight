from fastapi import FastAPI
from app.schemas import ExpenseCreate

app = FastAPI()

@app.post("/expenses")
def create_expense(expense: ExpenseCreate):
    return expense
