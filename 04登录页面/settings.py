from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
SQLALCHEMY_DB_URI = "sqlite:///./db2.db"
engine = create_engine(SQLALCHEMY_DB_URI,connect_args={"check_same_thread": False})


db_session =  sessionmaker(engine)
#Base.metadata.create_all(engine)


# Dependency
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()