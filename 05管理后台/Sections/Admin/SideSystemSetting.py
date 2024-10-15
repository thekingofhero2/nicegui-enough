from nicegui import ui ,app
from frame import frame
from Sections.Admin.PageAdminConf import LEFT_NAVS
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db
import os 
import json 

class SideSystemSetting:
    def __init__(self,db) -> None:
        self.page_title = "系统设置"
        self.db = db 

    

    def show(self,):
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            ui.label("系统设置页面")
            if app.storage.user['role'] != 0:
                ui.label("对不起，您没有权限修改系统设置！").classes("text-h3")
            else:
                ui.input("网站名称").bind_value(app.storage.user['site_conf'],"site_name")
                def save_auth(e):
                    with open('site.conf','w') as fpw:
                        json.dump(app.storage.user['site_conf'],fp=fpw)

                ui.button('保存网站信息', on_click=save_auth) 


@ui.page("/admin/systemsetting")
def side_system(db:Session = Depends(get_db)):
    """
    """
    page = SideSystemSetting(db)
    page.show()