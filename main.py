import flet as ft
from flet import (
    Page, Text, TextField, ElevatedButton, Container, Padding, Border, border,
    border_radius
)
from src.components.appbar import NavigationAppBar
from src.utils import routes_handler

from src.utils.requests_class import ApiRequest

"""
Minecraft id: 432
Documentacion = https://docs.curseforge.com/?python#curseforge-core-api-mods
base = https://api.curseforge.com
login = https://console.curseforge.com/#/login
"""


def main(page:ft.Page):
    page.title = "Minecraft Mods Downloader"
    page.theme_mode = ft.ThemeMode.DARK
    if not page.web:
        page.window_center()
        # page.window_min_width, page.window_min_height = 312, 124
        # page.window_width, page.window_height = 386, 201
        page.vertical_alignment = 'center'
        page.horizontal_alignment = 'center'
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            routes_handler(page)[page.route]
        )
    
    page.on_route_change = route_change
    page.go("/login")
    page.update()
    
    



ft.app(target=main,port=8550, view=ft.AppView.FLET_APP,)