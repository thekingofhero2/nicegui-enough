from nicegui import ui ,app
from UControls.WarnDialog import WarnDialog

def admin_required(func):
    def wrapped_func(*args,**kwargs):
        if app.storage.user['authenticated']:
            if app.storage.user["role"] == 0:
                return func(*args,**kwargs)
            else:
                dlg_warn = WarnDialog("警告","对不起，您没有权限修改系统设置！")
                dlg_warn.show()
                #ui.notify("对不起，您没有权限修改系统设置！",type="warning",position="center")
                #return ui.navigate.to('/')
    return wrapped_func