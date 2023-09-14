import flet as ft
from flet import (
    Page, Text, TextField, ElevatedButton, Row, Column, TextAlign, MainAxisAlignment, Container,
    colors, BorderRadius, Padding
)

def main(page:ft.Page):
    page.title = "Calculadora"
    page.vertical_alignment = MainAxisAlignment.CENTER.value
    page.window_height = 300
    page.window_width = 420
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
                        ElevatedButton(text="AC", expand=1,bgcolor=colors.WHITE12 ,  on_click=...),
                        ElevatedButton(text="+/-",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                        ElevatedButton(text="%",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                        ElevatedButton(text="/",expand=1,bgcolor=colors.WHITE12 , on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="7",expand=1, on_click=...),
                        ElevatedButton(text="8",expand=1, on_click=...),
                        ElevatedButton(text="9",expand=1, on_click=...),
                        ElevatedButton(text="*",expand=1, on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="4",expand=1, on_click=...),
                        ElevatedButton(text="5",expand=1, on_click=...),
                        ElevatedButton(text="6",expand=1, on_click=...),
                        ElevatedButton(text="-",expand=1, on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="3",expand=1, on_click=...),
                        ElevatedButton(text="2",expand=1, on_click=...),
                        ElevatedButton(text="1",expand=1, on_click=...),
                        ElevatedButton(text="+",expand=1, on_click=...),
                    ]),
                    Row([
                        ElevatedButton(text="0",expand=2, on_click=...),
                        ElevatedButton(text=".",expand=1, on_click=...),
                        ElevatedButton(text="=",expand=1, on_click=...),
                    ]),
                ]
            ),
        )
        
        
    )
    
    
    page.update()



ft.app(target=main,port=8550, view=ft.AppView.FLET_APP,)