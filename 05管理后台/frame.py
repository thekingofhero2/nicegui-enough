from nicegui import ui,app,client
from typing import List
from contextlib import contextmanager
from settings import Section,sections,LeftNav


def merge_leftnavs(left_navs :List[LeftNav]):
    """
    将left_navs按照expander_name进行合并，返回一个字典
    :params left_navs列表
    """
    left_navs_dict = {'N':[]}#"N"表示不需要包裹在expander中
    if len(left_navs) > 0:
        for left_nav_i in left_navs:
            if left_nav_i.expander_name is None:
                left_navs_dict['N'].append(left_nav_i)
            else:
                if left_nav_i.expander_name not in left_navs_dict.keys():
                    left_navs_dict[left_nav_i.expander_name] = []
                left_navs_dict[left_nav_i.expander_name].append(left_nav_i)
    return left_navs_dict            


#定义导航栏，并作为上下文，“套”在每个网页上
@contextmanager
def frame(nav_title :str,left_navs :List[Section] ,show_drawer):
    ui.page_title(nav_title)
    with ui.header().classes("glossy"):
        with ui.row().classes("w-full"):
            if  nav_title!="首页":
                ui.button(icon='menu',on_click=lambda :left_drawer.toggle() ).props('flat color=white')           
            with ui.link(target="/"):
                ui.button(f"{app.storage.user['site_conf']['site_name']}").props("flat").style("font-size:150%;font-width:300").classes("text-warning text-weight-bolder")
            for section in sections:
                #导航栏的每一个导航格，就是一个按钮
                with ui.link(target = section.uri):
                    """
                    flat:让button扁平化，没有四周的框
                    """
                    ui.button(section.section_name).props("flat").style("font-size:150%;font-width:300").classes("text-blue-grey-1 text-weight-bold")
            ui.space()
            
            #用户登录
            if  app.storage.user.get('authenticated', False):
                ui.label(f'你好 {app.storage.user["username"]}!').style("font-size:150%;font-width:300").classes("text-yellow-6")
                ui.button(on_click=lambda: (app.storage.user.clear(), ui.navigate.to('/'))
                        , icon='logout').props('outline round').classes("bg-red-8")
            else:
                ui.button(text="请登录",on_click=lambda: (app.storage.user.clear(), ui.navigate.to('/login'))
                        , icon='login').props('outline ')
    with ui.left_drawer(value = show_drawer).classes("bg-blue-grey-1") as left_drawer:
        if len(left_navs) > 0:
            left_navs_dict = merge_leftnavs(left_navs)
            #将不需要expander的标签页放在最上面
            for item in left_navs_dict['N']:
                if item.section_name is not None:
                    with ui.link(target = item.uri).classes("w-full"):
                        ui.button(item.section_name,icon="home").props("flat").classes("w-full justify-center text-blue-grey-10 text-h6")
                else:
                    ui.separator()
            left_navs_dict.pop("N")
            for expander_name in left_navs_dict.keys():
                with ui.expansion(expander_name, icon='tune').classes('w-full text-weight-bold'):
                    for item in left_navs_dict[expander_name]:
                        if item.section_name is not None:
                            with ui.link(target = item.uri):
                                ui.button(item.section_name).props("flat").classes("text-blue-grey-10")
                        else:
                            ui.separator()
        #生成器，
    yield