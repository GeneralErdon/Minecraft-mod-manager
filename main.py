import flet as ft
from flet import (
    Page, Text, TextField, ElevatedButton,
)

from src.utils.requests_class import ApiRequest

"""
Minecraft id: 432
"""


def main(page:ft.Page):
    page.title = "Minecraft Mods Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER.value
    
    page.update()



ft.app(target=main,port=8550, view=ft.AppView.FLET_APP,)