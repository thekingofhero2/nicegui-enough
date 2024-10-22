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

class Log(Base):
    __tablename__ = "user_log"
    __table_args__ = {
        "comment":"用户日志"
    }
    id = Column(Integer,primary_key=True,autoincrement=True,comment = "id表示每一条日志")
    uname = Column(VARCHAR(255) )#如果在尝试登录时，是没有uid的
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("User",backref="log_of_user")
    log_type = Column(Integer,comment="日志类型：0-登录日志（default） 1-操作日志。。。",default = 0)
    log_level = Column(Integer,comment="日志级别：0-info（default） 1-debug 2-warning 3-error。。。",default = 0)
    log_content = Column(Text,comment="日志内容")
    created_at = Column(DateTime, default=datetime.now())
