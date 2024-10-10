from settings import *
def init_db() -> None:
    Base.metadata.create_all(engine)


async def close_db() -> None:
    try:
        db_session.close_all()
    except:
        import traceback
        traceback.print_exc()