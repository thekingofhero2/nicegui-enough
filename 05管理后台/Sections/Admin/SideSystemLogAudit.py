from nicegui import ui ,app
from frame import frame
from Sections.Admin.PageAdminConf import LEFT_NAVS
from DB.CRUD import *
from fastapi import Request,Depends
from settings import get_db
from utils.LoginHelpers import admin_required
import os 
import json 

class SideSystemLogAudit:
    def __init__(self,db) -> None:
        self.page_title = "系统日志审计"
        self.db = db 

    
    @admin_required
    def show(self,):
        with frame(self.page_title,left_navs= LEFT_NAVS ,show_drawer=True):
            all_log = query_all_log(self.db)
            columns = [
                {'name': 'id', 'label': '日志id', 'field': 'id', 'required': True, 'align': 'left'},
                {'name': 'log_level', 'label': '日志级别', 'field': 'log_level', 'required': True, 'align': 'left'},
                {'name': 'log_level_org', 'label': '日志级别', 'field': 'log_level_org', 'required': True, 'align': 'left'},
                {'name': 'uname', 'label': '用户名', 'field': 'uname', 'sortable': True},
                {'name': 'log_type', 'label': '日志类别', 'field': 'log_type', 'sortable': True},
                {'name': 'log_content', 'label': '日志内容', 'field': 'log_content'},
                {'name': 'log_time', 'label': '创建时间', 'field': 'log_time', 'sortable': True},
            ]
            rows = all_log
            table = ui.table(columns=columns
                             , rows=rows
                             , row_key='id'
                             ,pagination = 10
                     , column_defaults={
                        'align': 'left',
                        'headerClasses': 'uppercase text-primary',
                    })
            """
            根据日志等级区分颜色，error-red,warning-yellow,其他-green
            """
            table.add_slot('body-cell-log_level', '''
                <q-td key="log_level" :props="props">
                    <q-badge :color= "props.value == 'error' ? 'red': props.value == 'warning' ? 'yellow' : 'green'  ">
                        {{ props.value }}
                    </q-badge>
                </q-td>
            ''')
         


@ui.page("/admin/systemlogaudit")
def side_systemlogaudit(db:Session = Depends(get_db)):
    """
    """
    page = SideSystemLogAudit(db)
    page.show()