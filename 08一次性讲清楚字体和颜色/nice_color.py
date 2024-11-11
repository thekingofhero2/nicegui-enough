from nicegui import ui 
## 1.颜色主题
## ①默认情况下
with ui.row().classes("w-full bg-primary justify-center"):
    ui.label("默认情况下").classes("bg-primary text-h1")
with ui.row().classes("w-full text-h2 text-white"):
    with ui.card().classes("bg-secondary"):
        ui.label("secondary").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")
    with ui.card().classes("bg-dark"):
        ui.label("dark").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")
    
    with ui.card().classes("bg-positive"):
        ui.label("positive").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")
    
    with ui.card().classes("bg-negative"):
        ui.label("negative").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")
    
    with ui.card().classes("bg-info"):
        ui.label("info").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")
    
    with ui.card().classes("bg-warning"):
        ui.label("warning").classes("text-capitalize")
        with ui.card_section():
            ui.label("随便一句话").classes("text-body1")

def change(e):
    import random
    def rand_color():
        return "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    ui.colors(primary = rand_color()
              , secondary = rand_color()
              , accent = rand_color()
              , dark = rand_color()
              , positive = rand_color()
              , negative = rand_color()
              , info = rand_color()
              , warning = rand_color())
ui.button("换主题",on_click=change)

ui.separator()
## 2.背景颜色举例（bg-颜色-色级）
with ui.row().classes("w-full").classes("bg-red-6"):
    ui.label("bg-red-6").classes("text-caption")
with ui.row().classes("w-full").classes("bg-red-8"):
    ui.label("bg-red-8").classes("text-caption")

## 3.文字颜色举例（text-颜色-色级）
with ui.row().classes("w-full").classes("bg-grey"):
    ui.label("text-red-6").classes("text-caption text-red-6")
with ui.row().classes("w-full").classes("bg-grey"):
    ui.label("text-red-8").classes("text-caption text-red-8")
ui.run()