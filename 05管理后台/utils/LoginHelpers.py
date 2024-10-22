from nicegui import ui ,app
from UControls.WarnDialog import WarnDialog
from DB.CRUD import check_user_exists

def admin_required(func):
    def wrapped_func(*args,**kwargs):
        if app.storage.user['authenticated']:
            if app.storage.user["role"] == 0:
                return func(*args,**kwargs)
            else:
                dlg_warn = WarnDialog("警告","对不起，您没有权限修改系统设置！")
                dlg_warn.show()
    return wrapped_func


def check_uname(db,username) -> None:  # local function to avoid passing username and password as arguments
    if not check_user_exists(db=db,uname = username):
        app.storage.client["register.check_uname"] = True
    else:
        app.storage.client["register.check_uname"] = False
        ui.notify("账户已存在",type="warning")