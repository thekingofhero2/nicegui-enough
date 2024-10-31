from nicegui import ui 
###3.2.1 盒子模型
ui.label("3.2.1 盒子模型").classes("text-h2")
ui.button("瘦按钮").classes("w-[50px] h-[100px]")
ui.button("胖按钮").classes("w-[100px] h-[100px]")
ui.button("高按钮").classes("w-[100px] h-[200px]")
ui.button("矮按钮").classes("w-[100px] h-[50px]")

ui.separator()
ui.label("3.2.2 外边距、内边距").classes("text-h2")
with ui.row().classes("bg-red"):
    ui.button("外边距按钮").classes("w-[100px] h-[100px] q-ma-lg")
    #ui.label("通过q-ma-lg，设置外边距（margin）、四周（all）、巨大间距（lg），所以露出了row的底色“红色”")
with ui.row().classes("bg-red"):
    ui.button("内边距按钮").classes("w-[100px] h-[100px] q-pa-lg")
    #ui.label("通过q-pa-lg，设置内边距（padding）、四周（all）、巨大间距（lg），所以文字被挤压换行了")




###3.2.2 盒子模型
ui.run()