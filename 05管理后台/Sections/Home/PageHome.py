from nicegui import ui ,app
from frame import frame
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db
import os 
import json 

class PageHome:
    def __init__(self,db) -> None:
        self.db = db
        self.page_title = "首页"

    def show(self):
        with frame(self.page_title,left_navs=[],show_drawer=False):
            with ui.grid(columns=4).classes("w-full"):
                for msg_obj_i in query_all_message(self.db):
                    with ui.card().tight():
                        ui.label(f"{msg_obj_i.uname}说:{msg_obj_i.msg_title}").classes("text-h6")
                        with ui.card_section():
                            ui.label(msg_obj_i.msg_content)


@ui.page("/")
def page_home(db:Session = Depends(get_db)):
    """
    默认进入的网页，首页
    """
    #加载网站配置
    def update_site_conf() :
        if os.path.exists('site.conf'):
            with open('site.conf') as fp:
                app.storage.user['site_conf'] = json.load(fp)
        else:
            app.storage.user['site_conf'] = {"site_name":"XXX后台管理系统"}
    update_site_conf()

    page = PageHome(db)
    page.show()
