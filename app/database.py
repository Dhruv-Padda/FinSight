from sqlalchemy import create_engine, text
from app.models import Base

DATABASE_URL = "postgresql://dhruv:password@localhost:5432/expense_tracker"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)