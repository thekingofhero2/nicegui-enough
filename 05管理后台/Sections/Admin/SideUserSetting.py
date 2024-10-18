from nicegui import ui ,app
from frame import frame
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db
from hashlib import md5 

from Sections.Admin.PageAdminConf import LEFT_NAVS

class SideUserSetting:
    def __init__(self,db) -> None:
        self.page_title = "用户设置"
        self.db = db 
    def show(self,):
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            ui.label("用户设置页面") 
            ui.label('1.密码修改，请一定更新密码!').classes("text-h2 text-red-6")
            p_org = ui.input("原密码",password=True)
            p1 = ui.input("新密码",placeholder="请一定记住",password=True,validation={'不要输入123456':lambda value: value != '123456'})
            p2 = ui.input("再次输入",placeholder="请一定记住",password=True,validation={'两次输入的不一致':lambda value:value ==p1.value})
            def save_pwd(e):
                if check_pwd(self.db,app.storage.user['username'],md5(p_org.value.encode("utf8")).hexdigest()) is None:
                    ui.notification("原密码错误",type="warning")
                elif p1.value == p2.value:
                    update_pwd(self.db ,app.storage.user['username'],md5(p2.value.encode("utf8")).hexdigest())
                    ui.notification("修改成功，请退出后重新登录",type="positive")
            ui.button('保存密码', on_click=save_pwd)


@ui.page("/admin/usersetting")
def side_usersetting(db:Session = Depends(get_db)):
    """
    """
    page = SideUserSetting(db)
    page.show()