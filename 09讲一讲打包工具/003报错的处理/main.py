from nicegui import native, ui,app
from pathlib import Path
ui.label('Hello from 稍微麻烦点儿')
ROOT = Path(__file__).parent
app.add_static_files("/assets", ROOT / "assets")
ui.image("/assets/gzh.png")
ui.run(reload=False, native=False,port=native.find_open_port())