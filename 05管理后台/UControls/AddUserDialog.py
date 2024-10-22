from nicegui import ui ,app
from DB.CRUD import *
from utils.LoginHelpers import check_uname 
from hashlib import md5 

class AddUserDialog:
    def __init__(self,db) -> None:
        """
        自定义增加用户Dialog
        
        """
        self.db = db 

    def show(self):
        with ui.dialog().classes("w-[600px] h-[600px]") as dialog, ui.card():
            with ui.card_section():
                ui.label("添加用户员").classes("text-h6 w-[300px]")
            with ui.card_section().classes("q-pt-none"):
                with ui.column().classes("w-full"):
                    ui_uname = ui.input("1.用户名",on_change=lambda e:check_uname(self.db,e.value))
                    ui_pwd = ui.input("2.密码",value="123456")
                    ui_role = ui.radio(["管理员","普通用户"],value="普通用户").props('inline')
            with ui.card_actions().classes("w-full justify-end"):
                ui.button('创建用户', on_click=lambda : self.add_user(ui_uname.value,ui_pwd.value,ui_role.value)).props("flat")
                ui.button('取消',on_click=dialog.close).props("flat")
        dialog.open()
    
    def add_user(self,uname,pwd,role):
        if len(uname) > 0:
            create_user(db=self.db,uname = uname,pwd=md5(pwd.encode("utf-8")).hexdigest(),role = 1 if role == '普通用户' else 0)
        else:
            ui.notify("用户名不能为空!",position="center",type="warning")
        ui.navigate.to("/admin/systemusermanage")