from nicegui import native, ui
from plugins.models.model_show import show
ui.label('Hello from 稍微麻烦点儿')
show()
ui.run(reload=False, native=False,port=native.find_open_port())