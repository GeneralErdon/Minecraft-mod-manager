import flet as ft
from flet import (
    UserControl, Page, ControlEvent, Row, Column,
    Container, IconButton, Icon, View, AppBar, Text,
    colors, icons,
)

class NavigationAppBar(AppBar):
    
    
    def __init__(self, page:Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        
        self.title = Text("Mod Manager", )
        self.center_title = True
        self.expand = True
        
        self.theme_change_btn = IconButton(
            icon=icons.LIGHT_MODE_ROUNDED,
            on_click=self.theme_change,
            )
        self.actions = [
            self.theme_change_btn
        ]
    
    def theme_change(self, e:ControlEvent):
        tema_actual = self.page.theme_mode
        if tema_actual == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_change_btn.icon = icons.DARK_MODE_ROUNDED
            
        elif tema_actual == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_change_btn.icon = icons.LIGHT_MODE_ROUNDED
        
        
        self.page.update()