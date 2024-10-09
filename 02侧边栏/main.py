from nicegui import ui 
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


#实例化网页，指明网页名、地址
left_navs = [
    Section("大屏展示","/bigtable"),
    Section("管理员","/admin"),
       
]
@ui.page("/")
def root_page():
    """
    默认进入的网页，首页
    """
    with frame():
        ui.label("这是首页")
@ui.page("/bigtable")
def root_bigtable_page():
    """
    大屏页面
    """
    with frame():
        ui.label("这是大屏页")
        with ui.grid(columns=2).classes("w-full"):
            ui.echart({
                'xAxis': {'type': 'category'},
                'yAxis': {'type': 'value'},
                'series': [{'type': 'line', 'data': [20, 10, 30, 50, 40, 30]}],
            })
            ui.echart({
                'xAxis': {'type': 'value'},
                'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
                'legend': {'textStyle': {'color': 'gray'}},
                'series': [
                    {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
                    {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
                ],
            })

            ui.echart({
                'xAxis': {'type': 'category'},
                'yAxis': {'axisLabel': {':formatter': 'value => "$" + value'}},
                'series': [{'type': 'line', 'data': [5, 8, 13, 21, 34, 55]}],
            })
            ui.echart({
                'xAxis': {'type': 'category', 'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']},
                'yAxis': {'type': 'value'},
                'series': [{'type': 'line', 'data': [150, 230, 224, 218, 135]}],
            })
@ui.page("/admin")
def root_admin_page():
    """
    默认进入的网页，首页
    """
    with frame():
        ui.label("管理员看到的页面")
@ui.page("/qita")
def qita_page():
    """
    """
    with frame():
        ui.label("这是其他页")

#定义导航栏，并作为上下文，“套”在每个网页上
@contextmanager
def frame():
    with ui.header():
        with ui.row():
            ##导航按钮
            ui.button(icon='menu',on_click=lambda :left_drawer.toggle() ).props('flat color=white')
            for section in sections:
                #导航栏的每一个导航格，就是一个按钮
                with ui.link(target = section.uri):
                    """
                    flat:让button扁平化，没有四周的框
                    """
                    ui.button(section.section_name).props("flat").classes("text-blue-grey-1")
    with ui.left_drawer(value = False).classes("bg-blue-grey-1") as left_drawer:
        for item in left_navs:
            if item.section_name is not None:

                        with ui.link(target = item.uri):
                            ui.button(item.section_name).props("flat").classes("text-blue-grey-10")
            else:
                ui.separator()
    #生成器，
    yield
ui.run()

