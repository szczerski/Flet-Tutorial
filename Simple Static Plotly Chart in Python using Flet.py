import flet as ft
from time import sleep
from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go


def main(page: ft.Page):

    page.title = "PyPl (2017 - 2022)"
    page.window_width = 700
    page.window_height = 600
    page.window_center()
    page.bgcolor = ft.colors.WHITE

    languages = [
        {"name": "Python", "color": ft.colors.YELLOW_600,
         "bgcolor": ft.colors.BLUE_800,
         "values": [15.2, 20.1, 25, 28.7, 30.2, 28.8]},
        {"name": "Java", "color": ft.colors.BLUE_800,
         "bgcolor": ft.colors.RED_800,
         "values": [
             22.9, 21.8, 21, 18.5, 16.7, 18.1]},
        {"name": "JavaScript", "color": "white",
         "bgcolor": ft.colors.YELLOW_600,
            "values": [8, 8.2, 8.1, 8.2, 8.4, 9.1]},
    ]

    years = [f"{i}" for i in range(2017, 2023)]

    def button_clicked(e):
        b.data += 1
        y = b.data
        if y < 6:
            chart.figure.data[0].labels = labels
            chart.figure.data[0].values = values[y]
            t.value = f"Year: {years[y]}"
            chart.update()
            page.update()

    labels = [lang["name"] for lang in languages]
    val = [lang["values"] for lang in languages]
    values = [list(i) for i in zip(*val)]

    t = ft.Text(color=ft.colors.BLUE_800, size=20)
    t.value = "Year: 2017"

    chart = PlotlyChart(
        go.Figure(data=[go.Pie(labels=labels,
                               values=values[0])]),
        expand=True)

    b = ft.ElevatedButton("Next Year",
                          on_click=button_clicked,
                          data=0)

    page.add(ft.Column(
        [
            ft.Container(content=chart,
                         width=700, height=400,
                         alignment=ft.alignment.center, ),
            ft.Container(t, alignment=ft.alignment.center,),
            ft.Container(b, alignment=ft.alignment.center,)]))


ft.app(target=main)
