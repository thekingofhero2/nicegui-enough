from nicegui import ui,app
##1.自定义字体 
### ①加载本地资源
app.add_static_files('/assets', r'./assets')
### ②将字体加载到网页头
ui.add_head_html(r'''
<!--思源黑体 Regular-->
<!--令东齐伋复刻体-->
<style>
@font-face{
    font-family: "customfont";
    src: url('/assets/fonts/SourceHanSansSC-Regular-2.otf') format('truetype');
    font-weight: normal;
    font-style: normal;
}
@font-face{
    font-family: "lingdong-font";
    src: url('/assets/fonts/LingDongQiCheChunTang-2.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}
</style>

''')
### ③声明自定义css类型
ui.add_css("""
.my-font {
  font-family: 'customfont';
}
.my-font-lindong {
  font-family: 'lingdong-font';
}
""")
### ④看效果
ui.label('你好').classes("text-h1")
ui.label('你好').classes("text-h1").classes("my-font")
ui.label("你好").classes("text-h1").classes("my-font-lindong")


ui.separator()
##2.Quasar内置的字体大小设置
with ui.grid(columns=2):
    ui.label("text-h1")
    ui.label("一级标题").classes("text-h1")

    ui.label("text-h2")
    ui.label("二级标题").classes("text-h2")

    ui.label("text-h3")
    ui.label("三级标题").classes("text-h3")

    ui.label("text-h4")
    ui.label("四级标题").classes("text-h4")

    ui.label("text-h5")
    ui.label("五级标题").classes("text-h5")

    ui.label("text-h6")
    ui.label("六级标题").classes("text-h6")

    ui.label("text-subtitle1")
    ui.label("一级子标题").classes("text-subtitle1")

    ui.label("text-subtitle2")
    ui.label("二级子标题").classes("text-subtitle2")

    ui.label("text-body1")
    ui.label("一类正文").classes("text-body1")

    ui.label("text-body2")
    ui.label("二类正文").classes("text-body2")

ui.separator()
##3.Quasar内置的字的轻重
with ui.grid(columns=2):
    ui.label("text-weight-thin")
    ui.label("很轻").classes("text-weight-thin")

    ui.label("text-weight-light")
    ui.label("一般轻").classes("text-weight-light")

    ui.label("text-weight-regular")
    ui.label("普通").classes("text-weight-regular")

    ui.label("text-weight-medium")
    ui.label("中等").classes("text-weight-medium")

    ui.label("text-weight-bold")
    ui.label("一般重").classes("text-weight-bold")

    ui.label("text-weight-bolder")
    ui.label("很重").classes("text-weight-bolder")
ui.separator()
##4.字的对齐方式
with ui.grid(columns=2):
    ui.label("默认情况")
    ui.label("我是一句正常的话，这句话很长").classes("text-h1")

    ui.label("text-right")
    ui.label("我是一句正常的话，这句话很长").classes("text-h1 bg-grey text-right")
    
    ui.label("text-left")
    ui.label("我是一句正常的话，这句话很长").classes("text-h1 bg-grey-2 text-left")

    ui.label("text-center")
    ui.label("我是一句正常的话，这句话很长").classes("text-h1 bg-grey-4 text-center")

    ui.label("text-no-wrap")
    ui.label("我是一句正常的话，这句话很长").classes("text-h1 bg-grey-6 text-no-wrap")

ui.separator()
##5.手动修改字体大小 
ui.label("默认大小").classes("text-h1")
ui.label("默认大小").classes("text-h1").style("font-size: 40px;")
ui.run()