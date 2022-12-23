import flet as ft


def main(page):

    def set_important(e):
        e.control.selected = not e.control.selected
        e.control.update()

    def add_txt(e):
        txt = new_txt.value
        if btn_important.selected:
            txt += "❗"
        txt_view.controls.append(ft.Text(txt))
            
        new_txt.value = ""
        new_txt.focus()
        view.update()

    def on_hover(e):
        e.control.bgcolor = "indigo500" if e.data == "true" else "indigo300"
        e.control.update()

    def on_long_press(e):
        e.control.bgcolor = "indigo300" if e.data == "true" else "indigo900"
        e.control.update()

    txt_view = ft.Column()
    new_txt = ft.TextField(autofocus=True)
    button = ft.IconButton(
        autofocus=True,
        # bgcolor="deeporangeaccent700",
        # color="onSecondaryContainer",
        # elevation=0.5,
        icon=ft.icons.ADD,
        # icon_color="amber",
        # text="add",
        # tooltip="Add a new txt",
        # rotate=.4,
        # visible=False,
        # disabled=True,
        # opacity=.8,
        # scale=1.5,
        # offset=ft.transform.Offset(-1,-.3),
        # expand=True,
        # height=70,
        # width=100,
        # style=ft.ButtonStyle(
        #     shape=ft.BeveledRectangleBorder(radius=20),
        # ),
        # style=ft.ButtonStyle(
        #         shape=ft.RoundedRectangleBorder(radius=10),
        # ),



        on_click=add_txt,
        # on_hover=on_hover,
        # on_long_press=on_long_press

    )
    btn_important = ft.IconButton(
        icon=ft.icons.NOTIFICATION_IMPORTANT_ROUNDED,
        selected=False,
        style=ft.ButtonStyle(color={"selected": ft.colors.ORANGE,
                                    "hovered": ft.colors.GREEN}),
        on_click=set_important,
    )

    view = ft.Column([ft.Row([new_txt, button, btn_important]),
                      txt_view])
    page.add(view)


ft.app(target=main)