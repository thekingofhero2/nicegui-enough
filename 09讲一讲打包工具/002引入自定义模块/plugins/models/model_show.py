from nicegui import ui
from plugins.models.ss import ss
def show():
    ui.label("我是model_show").classes("text-red-5")
    ss()