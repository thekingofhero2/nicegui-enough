import DB.Models as models
from sqlalchemy.orm import Session

def check_pwd(db :Session,uname:str,pwd:str):
    first = db.query(models.User).filter(models.User.uname == uname).first()
    if first is not None:
        return first.pwd == pwd
    return False 

def check_user_exists(db :Session,uname:str):
    q = db.query(models.User).filter(models.User.uname == uname)
    return db.query(q.exists()).scalar()


def create_user(db :Session,uname:str,pwd:str):
    user = models.User(uname=uname,pwd=pwd)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user