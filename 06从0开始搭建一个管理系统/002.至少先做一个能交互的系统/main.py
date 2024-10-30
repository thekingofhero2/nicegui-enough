from nicegui import ui 
from fastapi import Depends
from DB.CRUD import * 
from DB.DB import init_db,close_db
from settings import *

#1.在应用启动时，初始化数据库（定义数据表，这里用的是sqlite，会自动创建db2.db文件）
app.on_startup(init_db)
#2.在应用销毁时，关闭数据库连接
app.on_shutdown(close_db)

@ui.page("/")
def main(db:Session = Depends(get_db)):
    ui.label("发帖")
    ui_input_name = ui.input("用户名:")
    ui_input_title = ui.input("帖子标题:")
    ui_text_msg_content = ui.textarea("帖子内容:")
    ui.button("发布",on_click=lambda :create_message(db=db_session(),uname=ui_input_name.value,msg_title=ui_input_title.value,msg_content=ui_text_msg_content.value))
    ui.separator()
    ui.label("看帖")
    """
    所有人的帖子
    """
    with ui.grid(columns=4).classes("w-full"):
        for msg_obj_i in query_all_message(db_session()):
            with ui.card().tight():
                ui.label(f"{msg_obj_i.uname}说:{msg_obj_i.msg_title}").classes("text-h6")
                with ui.card_section():
                    ui.label(msg_obj_i.msg_content)
ui.run()