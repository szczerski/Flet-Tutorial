import flet as ft


DICTIONARY = {'dog': 'hund', 'cat': 'katze',
              'deer': 'hirsch', 'duck': 'ente',
              }

SENTENCES = {'hund': 'Der Hund hat einen Knochen',
             'katze': 'Katze trinkt Milch',
             'hirsch': 'Ein Hirsch läuft durch den Wald',
             'ente': 'Enten fliegen in den Wald'}


def main(page: ft.Page):
    page.title = "English-German Dictionary"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.window_width = 300
    # page.window_height = 350
    # page.window_center()

    def print_sentence(e):
        word = e.control.data
        meaning = DICTIONARY[word]
        sentences = SENTENCES[meaning]
        page.controls[2].content = ft.Text(
            word + " 👉 " + meaning + " \n📚 SENTENCE: " + sentences,
            size=25, color=ft.colors.BLUE_800)

        page.update()

    def textbox_changed(string):
        str_lower = string.control.value.lower()
        list_view.controls = [
            list_items.get(dict_word) for dict_word
            in DICTIONARY if str_lower in dict_word.lower()
        ] if str_lower else []
        page.update()

    list_items = {
        word: ft.ListTile(
            title=ft.Text(
                word + " : " + DICTIONARY[word],
                size=20, color=ft.colors.BLUE_500),
            leading=ft.Icon(ft.icons.ARROW_FORWARD),
            on_click=print_sentence, data=word
        )
        for word in DICTIONARY
    }

    text_field = ft.TextField(label="Search word:",
                              width=500, on_change=textbox_changed)
    list_view = ft.ListView(expand=1, spacing=10, padding=20)
    sentences_view = ft.Container(content=ft.Text("Select a word to see the sentence.",
                                                  size=20, color=ft.colors.BLUE_500),
                                  )

    page.add(text_field, list_view, sentences_view)


# ft.app(target=main, view=ft.WEB_BROWSER, port=8484)
ft.app(target=main)
