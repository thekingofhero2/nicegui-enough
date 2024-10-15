from settings import Base,SQLALCHEMY_DB_URI
from sqlalchemy import Column,BIGINT,VARCHAR,Integer,ForeignKey,Text,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(VARCHAR(255) )
    pwd = Column(VARCHAR(64))
    role = Column(Integer,comment = "角色：0-管理员 1-普通用户",default = 1)


class Message(Base):
    __tablename__ = "user_message"
    __table_args__ = {
        "comment":"用户发的消息"
    }
    id = Column(Integer,primary_key=True,autoincrement=True,comment = "id表示每一个消息")
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("User",backref="message_of_user")
    msg_title = Column(VARCHAR(255),comment="标题")
    msg_content = Column(Text,comment="内容")
    created_at = Column(DateTime, default=datetime.now())

