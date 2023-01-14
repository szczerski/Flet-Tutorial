import flet as ft
import random
import time


def main(page: ft.Page):
    page.title = "Memo Game"
    page.window_height = 710
    page.window_width = 910

    number_of_single_cards: int = 20

    global idx_of_cards

    list_of_pairs = []
    find = []
    image_page = "https://picsum.photos/id/"

    def make_cards(number_of_single_cards):
        card_deck_with_duplicates = \
            [f"{i}_A" for i in range(number_of_single_cards)] + \
            [f"{i}_B" for i in range(number_of_single_cards)]
        random.shuffle(card_deck_with_duplicates)
        return card_deck_with_duplicates

    idx_of_cards = make_cards(number_of_single_cards)

    def start_game(e):

        start_button.disabled = True

        global start_time
        start_time = time.time()

        # make reverse cards
        for i in range(len(idx_of_cards)):
            row_board.controls[i].content = None
            row_board.controls[i].bgcolor = ft.colors.AMBER
            row_board.controls[i].border_radius = \
                ft.border_radius.all(10)
            page.update()

    def match_pairs(e):
        if len(list_of_pairs) == 2:
            return

        if start_button.disabled:
            num = e.control.data

            idx = idx_of_cards[num].split('_')[0]
            index_a = idx_of_cards.index(str(idx)+'_A')
            index_b = idx_of_cards.index(str(idx)+'_B')
            index_of_image_ = idx_of_cards[num].split("_")[0]

            if len(list_of_pairs) < 2:
                row_board.controls[num].content = ft.Image(src=f"{image_page+'1'+index_of_image_}/100",
                                                           border_radius=ft.border_radius.all(10))
                if idx_of_cards[num] not in list_of_pairs:
                    list_of_pairs.append(idx_of_cards[num])

            page.update()

            if len(list_of_pairs) == 2:

                a = int(list_of_pairs[0].split('_')[0])
                b = int(list_of_pairs[1].split('_')[0])

                if a == b:
                    time.sleep(.4)

                    for index in (index_a, index_b):
                        row_board.controls[index].disabled = True
                        row_board.controls[index].content = None
                        row_board.controls[index].bgcolor = ft.colors.BLACK

                    find.append(index_a)

                    if len(find) == number_of_single_cards:
                        stop_time = time.time()

                        start_button.text = "Time: \n{} \nseconds".format(
                            str(round(stop_time - start_time, 0)))
                        page.update()

                    page.update()
                    list_of_pairs.clear()
                else:
                    time.sleep(1)
                    flip_a = idx_of_cards.index(list_of_pairs[0])
                    flip_b = idx_of_cards.index(list_of_pairs[1])

                    for index in (flip_a, flip_b):
                        row_board.controls[index].content = None
                        row_board.controls[index].bgcolor = ft.colors.AMBER

                    list_of_pairs.clear()
                    page.update()

            page.update()

    def board(idx_of_cards):
        card_images = []

        for num in range(len(idx_of_cards)):

            index_of_image = idx_of_cards[num].split("_")[0]

            card_images.append(
                ft.Container(
                    content=ft.Image(src=f"{image_page+'1'+index_of_image}/100",
                                     border_radius=ft.border_radius.all(10)),
                    width=100,
                    height=100,
                    data=num,
                    on_click=match_pairs
                )
            ),
        return card_images

    row_board = ft.Row(wrap=True, controls=board(idx_of_cards))
    start_button = ft.ElevatedButton(text="Play", width=100, data='play',
                                     height=100, on_click=start_game)
    page.add(row_board, start_button)


ft.app(target=main)
