from nicegui import native, ui,app
from pathlib import Path
ui.label('Hello from splash~~')

try:
        import pyi_splash
        pyi_splash.update_text('UI Loaded ...')
        pyi_splash.close()
except:
    pass
ui.run(reload=False, native=False,port=native.find_open_port())