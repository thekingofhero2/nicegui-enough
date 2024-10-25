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
                ui.button("提交",on_click=lambda x: self.create_msg(uid = uid,msg_title=ui_msg_title.value,msg_content=ui_msg_content.value))
            ui.separator()
            with ui.row().classes("w-full justify-center"):
                ui.label("本站所有人的说说:").classes("text-h6 text-secondary")
            self.show_all()

    @ui.refreshable
    def show_all(self,):
        """
        所有人的说说
        """
        with ui.grid(columns=4).classes("w-full"):
                for msg_obj_i in query_all_message(self.db):
                    with ui.card().tight():
                        ui.label(f"{msg_obj_i.uname}说:{msg_obj_i.msg_title}").classes("text-h6")
                        with ui.card_section():
                            ui.label(msg_obj_i.msg_content)
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


    def create_msg(self,uid,msg_title,msg_content):
        create_message(self.db,uid = uid,msg_title=msg_title,msg_content=msg_content)
        self.show_all.refresh()

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