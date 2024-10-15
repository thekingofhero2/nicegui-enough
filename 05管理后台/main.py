from Sections.Admin.PageAdmin import page_admin
from Sections.Home.PageHome import page_home
from nicegui import ui,app,Client
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from Login import login
from DB.DB import init_db,close_db
from settings import unrestricted_page_routes,ROOT
import os 
import json


#2.认证中间件（这部分改的官方样例），用来判断登录状态，及未认证情况下的操作
class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        #3.判断是否登录
        if not app.storage.user.get('authenticated', False):
            #4.如果未登录，并且页面需要登录后可见，就重定向到login页面
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path 
                return RedirectResponse('/login')
        return await call_next(request)



#5.在应用启动时，初始化数据库（定义数据表，这里用的是sqlite，会自动创建db2.db文件）
app.on_startup(init_db)
#6.在应用销毁时，关闭数据库连接
app.on_shutdown(close_db)
#7.挂载“认证中间件”
app.add_middleware(AuthMiddleware)


ui.run(storage_secret="abc",favicon= ROOT / "assets" / "favicon.png")