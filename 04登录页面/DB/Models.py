from settings import Base,SQLALCHEMY_DB_URI
from sqlalchemy import Column,BIGINT,VARCHAR,Integer
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(VARCHAR(255) )
    pwd = Column(VARCHAR(64))