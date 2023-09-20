import flet as ft
from flet import (
    Page, Text, TextField, ElevatedButton, Row, Column, TextAlign, MainAxisAlignment, Container,
    colors, BorderRadius, Padding
)

def main(page:ft.Page):
    page.title = "Calculadora"
    #page.vertical_alignment = MainAxisAlignment.CENTER.value
    # page.window_height = 300
    # page.window_width = 420
    
    page.window_top = 500
    page.window_left = 500
    page.window_max_height = 300
    page.window_max_width = 420
    
    def write_num(n:str) -> None:
        if result_txt.value == "0":
            result_txt.value = n
            return result_txt.update()
        result_txt.value += n
        return result_txt.update()
    
    def clear(e):
        result_txt.value = "0"
        result_txt.update()
    
    
    
    result_txt = Text(value="0", disabled=True, text_align=TextAlign.RIGHT, color=colors.WHITE, size=20)
    
    page.add(
        Container(
            bgcolor=colors.BLACK,
            border_radius=BorderRadius(10,10,10,10),
            padding= Padding(20,20,20,20),
            content=Column(
                controls=[
                    Row(controls=[result_txt], alignment=MainAxisAlignment.END ),
                    Row([
                        ElevatedButton(text="AC", expand=1,bgcolor=colors.WHITE12 ,  on_click=clear),
                        ElevatedButton(text="+/-",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                        ElevatedButton(text="%",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                        ElevatedButton(text="/",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="7",expand=1, on_click=lambda e: write_num("7")),
                        ElevatedButton(text="8",expand=1, on_click=lambda e: write_num("8")),
                        ElevatedButton(text="9",expand=1, on_click=lambda e: write_num("9")),
                        ElevatedButton(text="*",expand=1, on_click=lambda e: write_num("*")),
                    ]),
                    Row([
                        ElevatedButton(text="4",expand=1, on_click=lambda e: write_num("4")),
                        ElevatedButton(text="5",expand=1, on_click=lambda e: write_num("5")),
                        ElevatedButton(text="6",expand=1, on_click=lambda e: write_num("6")),
                        ElevatedButton(text="-",expand=1, on_click=lambda e: write_num("-")),
                    ]),
                    Row([
                        ElevatedButton(text="3",expand=1, on_click=lambda e: write_num("3")),
                        ElevatedButton(text="2",expand=1, on_click=lambda e: write_num("2")),
                        ElevatedButton(text="1",expand=1, on_click=lambda e: write_num("1")),
                        ElevatedButton(text="+",expand=1, on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="0",expand=2, on_click=lambda e: write_num("0")),
                        ElevatedButton(text=".",expand=1, on_click=...),
                        ElevatedButton(text="=",expand=1, on_click=...),
                    ]),
                ]
            ),
        )
    )
    



ft.app(target=main,port=8550, view=ft.AppView.FLET_APP,)