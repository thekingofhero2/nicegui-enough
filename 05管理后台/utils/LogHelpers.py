from nicegui import ui ,app
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('system')
logger.setLevel(logging.ERROR)
fh = TimedRotatingFileHandler('system.log', maxBytes=1024*1024, backupCount=1)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.INFO)


def system_log(func,log_type):
    """
    未完成
    """
    def wrapped_func(*args, **kwargs):
        logger.info("")
        return func(*args, **kwargs)
        
    return wrapped_func
