from nicegui import ui,app 


class WarnDialog:
    def __init__(self,header,content,close_redirect = '/') -> None:
        """
        自定义告警Dialog
        :param header: 表示告警框显示的头
        :param content: 告警内容 
        :param close_redirect: 关闭按钮后重定向到哪个页面，默认跳转到 /
        """
        self.header = header
        self.content = content
        self.close_redirect = close_redirect
        self.dialog = ui.dialog()
        self.dialog_card = ui.card()
    def show(self):
        with self.dialog, self.dialog_card:
            with ui.card_section():
                ui.label(self.header).classes("text-h6")
            with ui.card_section().classes("q-pt-none"):
                ui.label(self.content)
            ui.button('Close', on_click= ui.navigate.to(self.close_redirect) )
        self.dialog.open()
