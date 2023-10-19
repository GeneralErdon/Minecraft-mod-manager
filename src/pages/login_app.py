import flet as ft
from flet import (
    UserControl, Page, ControlEvent, Row, Column,
    Container, IconButton, Icon, View, Text, MainAxisAlignment as Align, alignment, padding,
    colors, icons,
)


class LoginPage(UserControl):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.expand = True
    
    def build(self):
        return Container(
            bgcolor=colors.BLUE_900,
            content=Column([
                Text("AAAAAAAAAAA"),
                ],
                alignment=Align.CENTER,
                horizontal_alignment=Align.CENTER,
            ),
            alignment=alignment.center,
            padding=padding.all(10),
        )
