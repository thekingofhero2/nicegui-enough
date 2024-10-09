from nicegui import ui 
"""
本节内容：修改网页基础信息
"""
#1.修改网页元数据。shared是表示是否所有网页都复用相同信息
ui.add_head_html("""<meta name="description" content="本网站是一个学习nicegui的网站"/>""",shared=True)
ui.add_head_html("""<meta name="keywords" content="nicegui,enough,learn"/>""",shared=True)

#2.网页标题
ui.page_title("敲键盘的生活")

ui.label("测试页")

#3.favicon的修改
ui.run(port=9999,favicon="favicon.png",reload=False)