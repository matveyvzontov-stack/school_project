from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

# Create Database Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a scoped Local Session layer
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our Models
Base = declarative_base()

# Dependency to yield direct connection sessions safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
