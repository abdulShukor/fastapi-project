from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlCHEMY_DATBASE_URL = 'postgresql://<user>:<password>:@<ip-address/hostname>/'
SQLAlCHEMY_DATBASE_URL = 'postgresql+psycopg://postgres:admin@localhost/fastapi'
engine = create_engine(SQLAlCHEMY_DATBASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()