from nicegui import ui ,app
from frame import frame
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db
from hashlib import md5 

from Sections.Admin.PageAdminConf import LEFT_NAVS

class SideUserContent:
    def __init__(self,db) -> None:
        self.page_title = "用户内容编辑"
        self.db = db 
    def show(self,):
        uid = app.storage.user["uid"]
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            ui.label('编辑已发布内容').classes("text-h2 ")
            with ui.grid(columns=4).classes("w-full"):
                for msg_obj_i in query_all_message_by_uid(self.db,uid):
                    with ui.card().tight():
                        ui.label(f"{msg_obj_i.uname}说:{msg_obj_i.msg_title}").classes("text-h6")
                        with ui.card_section():
                            ui.label(msg_obj_i.msg_content)
                        with ui.card_actions():
                            ui.button("编辑",on_click=lambda x:ui.navigate.to(f"/adminedit/{msg_obj_i.id}"))


@ui.page("/admin/usercontent")
def side_usercontent(db:Session = Depends(get_db)):
    """
    """
    page = SideUserContent(db)
    page.show()