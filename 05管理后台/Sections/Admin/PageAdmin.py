from nicegui import ui ,app
from frame import frame
from Sections.Admin.PageAdminConf import LEFT_NAVS
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db

"""
显示引用相关路由
"""
from Sections.Admin.SideSystemSetting import side_system
from Sections.Admin.SideUser import side_user

class PageAdmin:
    def __init__(self,db) -> None:
        self.page_title = "系统管理"
        self.db = db
        
    def show(self):
        uid = app.storage.user["uid"]
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            with ui.column():
                ui_msg_title = ui.input("输入信息名称")
                ui_msg_content = ui.textarea("输入信息内容")
                ui.button("提交",on_click=lambda x: create_message(self.db,uid = uid,msg_title=ui_msg_title.value,msg_content=ui_msg_content.value))

@ui.page("/admin")
def page_admin(db:Session = Depends(get_db)):
    """
    """
    page = PageAdmin(db)
    page.show()
    