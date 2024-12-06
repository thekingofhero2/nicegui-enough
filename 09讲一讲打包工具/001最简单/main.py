from nicegui import native, ui

ui.label('Hello from PyInstaller')

ui.run(reload=False, native=False,port=native.find_open_port())