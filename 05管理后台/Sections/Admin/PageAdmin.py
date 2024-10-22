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
from Sections.Admin.SideSystemUserManage import side_systemusermanage
from Sections.Admin.SideSystemLogAudit import side_systemlogaudit
from Sections.Admin.SideUserSetting import side_usersetting
from Sections.Admin.SideUserContent import side_usercontent

class PageAdmin:
    def __init__(self,db,msg_id=None) -> None:
        self.page_title = "系统管理"
        self.db = db
        self.msg_id = msg_id
        
    def show(self):
        uid = app.storage.user["uid"]
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            with ui.column():
                ui_msg_title = ui.input("输入信息名称")
                ui_msg_content = ui.textarea("输入信息内容")
                ui.button("提交",on_click=lambda x: create_message(self.db,uid = uid,msg_title=ui_msg_title.value,msg_content=ui_msg_content.value))
    def show_edit(self):
        if self.msg_id is not None:
            msg_item = query_message_by_id(self.db,self.msg_id)
        if msg_item:
            with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
                with ui.column():
                    ui_msg_title = ui.input("输入信息名称",value = msg_item.msg_title)
                    ui_msg_content = ui.textarea("输入信息内容",value = msg_item.msg_content)
                    ui.button("编辑",on_click=lambda x: update_message(self.db,id = self.msg_id,msg_title=ui_msg_title.value,msg_content=ui_msg_content.value))
        else:
            self.show()

@ui.page("/admin")
def page_admin(db:Session = Depends(get_db)):
    """
    """
    page = PageAdmin(db)
    page.show()


@ui.page("/adminedit/{msg_id}")
def page_admin(db:Session = Depends(get_db),msg_id = 1):
    """
    编辑现有的msg
    """
    page = PageAdmin(db,msg_id)
    page.show_edit()