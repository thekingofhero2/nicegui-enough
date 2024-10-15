from settings import *
from DB.CRUD import *
from hashlib import md5
def init_db() -> None:
    Base.metadata.create_all(engine)
    db = db_session()
    if not check_user_exists(db,"admin"):
        create_user(db=db,uname = "admin",pwd=md5(b"123456").hexdigest(),role=0)


async def close_db() -> None:
    try:
        db_session.close_all()
    except:
        import traceback
        traceback.print_exc()