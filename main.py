from flet import *
from summup import *


def main(page: Page):
    page.title = "Squeegee"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = colors.BLACK
    page.window_width = 400
    page.window_height = 300

    def btn_click(e):
        if not txt.value:
            txt.error_text = "Please Enter text"
            page.update()
        else:
            text = txt.value
            out_txt.value = text_sumup(text)
            out_txt.clean()
            page.update()


    txt = TextField(label='Enter text to Squeez', border_width=2)
    page.add(
        Column
            (controls=[txt, ElevatedButton('Text Summarization', on_click=btn_click)]))
    out_txt = Text(
                   size=20,
                   color=colors.WHITE,
                   weight=FontWeight.NORMAL, )
    page.add(out_txt)
    page.update()


app(target=main,assets_dir="assets",view=AppView.WEB_BROWSER)
