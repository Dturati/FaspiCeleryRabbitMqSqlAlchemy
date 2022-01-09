from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://admin:123@localhost:5432/fastapi",
    # connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()