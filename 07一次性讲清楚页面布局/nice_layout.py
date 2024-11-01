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

ui.separator()
ui.label("3.2.3 网格布局").classes("text-h2")
with ui.grid(columns=12):
    #通过设置col-span-X,限定每一列宽度
    ui.button("普通按钮").classes("col-span-1")
    ui.button("普通按钮").classes("col-span-2")
    ui.button("普通按钮").classes("col-span-6")
    ui.button("普通按钮").classes("col-span-8")
    ui.button("普通按钮").classes("col-span-4")
    ui.button("普通按钮").classes("col-span-1 h-[300px]")
    ui.button("普通按钮").classes("col-span-1")

ui.label("3.2.4 网格行").classes("text-h2")
with ui.row().classes("bg-red"):
    ui.button("普通按钮")
with ui.row().classes("w-full bg-red"):
    ui.button("普通按钮")
with ui.row().classes("w-full bg-red"):
    ui.button("普通按钮").classes("h-[300px]")
    ui.button("普通按钮")

with ui.column().classes("bg-red"):
    ui.button("普通按钮1")
    ui.button("普通按钮2")
    ui.button("普通按钮3")

with ui.column().classes("w-full bg-red"):
    ui.button("普通按钮1").classes("w-[300px]")
    ui.button("普通按钮2").classes("h-[300px]")
    ui.button("普通按钮3")

###3.2.2 盒子模型
ui.run()