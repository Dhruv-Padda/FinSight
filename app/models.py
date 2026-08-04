
from sqlalchemy import Integer, String, ForeignKey, CheckConstraint, Date, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date, datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)


class Expense(Base):
    __tablename__ = "expenses"
    __table_args__ = (CheckConstraint("amount>0", name = "check_positive_amount"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(String(50),nullable = False)
    description: Mapped[str|None] = mapped_column(nullable=True)
    date: Mapped[date] = mapped_column(Date,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now())




