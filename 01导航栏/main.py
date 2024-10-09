from nicegui import ui
from dataclasses import dataclass,field
from contextlib import contextmanager

@dataclass
class Section:
    """
    定义网页数据类型
    """
    section_name :str #网页名
    uri :str #网页地址

#实例化网页，指明网页名、地址
sections = [
    Section("首页","/"),
    Section("其它页","/qita"),
       
]

@ui.page("/")
def root_page():
    """
    默认进入的网页，首页
    """
    with frame():
        ui.label("这是首页")

@ui.page("/qita")
def root_page():
    """
    """
    with frame():
        ui.label("这是其它页")

#定义导航栏，并作为上下文，“套”在每个网页上
@contextmanager
def frame():
    with ui.header():
        with ui.row():
            for section in sections:
                #导航栏的每一个导航格，就是一个按钮
                with ui.link(target = section.uri):
                    """
                    flat:让button扁平化，没有四周的框
                    """
                    ui.button(section.section_name).props("flat").classes("text-blue-grey-1")
    #生成器，
    yield

ui.run()