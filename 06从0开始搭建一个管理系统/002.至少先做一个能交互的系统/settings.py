from dataclasses import dataclass,field
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from nicegui import app 



#######基本配置(不用修改)###########
ROOT = Path(__file__).parent

#########################

######数据库相关配置#####
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
########################




