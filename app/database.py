from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
import time
from .config import settings

# SQLAlCHEMY_DATBASE_URL = 'postgresql://<user>:<password>:@<ip-address/hostname>/'
SQLAlCHEMY_DATBASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

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


# while True:
#     try:
#      conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='admin')
#      cursor = conn.cursor()
#      print("Database connection was successfull!")
#      break
#     except Exception as error:
#      print("Connecting to database failed")
#      print("Error", error)
#      time.sleep(2)