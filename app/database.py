from sqlalchemy import create_engine
from app.models import Base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://dhruv:password@localhost:5432/expense_tracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)