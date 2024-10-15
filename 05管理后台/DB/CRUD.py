import DB.Models as models
from sqlalchemy.orm import Session

def check_pwd(db :Session,uname:str,pwd:str):
    whoami = db.query(models.User).filter(models.User.uname == uname).first()
    if whoami is not None \
        and whoami.pwd == pwd:
        return (whoami.id,whoami.role)
    return None

def update_pwd(db :Session,uname:str,pwd:str):
    whoami = db.query(models.User).filter(models.User.uname == uname).first()
    whoami.pwd = pwd
    db.commit()
    
    return True

def check_user_exists(db :Session,uname:str):
    q = db.query(models.User).filter(models.User.uname == uname)
    return db.query(q.exists()).scalar()


def create_user(db :Session,uname:str,pwd:str,role:int=1):
    user = models.User(uname=uname,pwd=pwd,role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

##############Message#########
def create_message(db :Session,uid :str,msg_title:str,msg_content:str):
    msg = models.Message(user_id = uid,msg_title=msg_title ,msg_content=msg_content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def query_all_message(db :Session):
    all = db.query( models.Message.msg_title,models.Message.msg_content,models.User.uname).join(models.User).all()
    return all
