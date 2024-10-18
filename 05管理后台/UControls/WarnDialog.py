from nicegui import ui 


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
    def show(self):
        with ui.dialog() as dialog, ui.card():
            with ui.card_section():
                ui.label(self.header).classes("text-h6")
            with ui.card_section().classes("q-pt-none"):
                ui.label(self.content)
            with ui.card_actions().classes("w-full justify-end"):#.props("align=right"):
                ui.button('ok', on_click=lambda : ui.navigate.to(self.close_redirect) ).props("flat")
        dialog.open()
