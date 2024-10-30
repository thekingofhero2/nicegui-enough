import DB.Models as models
from sqlalchemy.orm import Session


def check_user_exists(db :Session,uname:str):
    user = db.query(models.User).filter(models.User.uname == uname).first()
    if user is None:
        return False 
    else:
        return user


def create_user(db :Session,uname:str,pwd:str="123456",role:int=1):
    user = models.User(uname=uname,pwd=pwd,role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


##############Message#########
def create_message(db :Session,uname :str,msg_title:str,msg_content:str):
    user = check_user_exists(db=db,uname=uname)
    if not user :
        user = create_user(db ,uname)
    msg = models.Message(user_id = user.id,msg_title=msg_title ,msg_content=msg_content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def query_all_message(db :Session):
    all = db.query( models.Message.msg_title,models.Message.msg_content,models.User.uname).join(models.User).all()
    return all


