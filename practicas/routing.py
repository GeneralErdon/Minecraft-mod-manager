from typing import Any, List, Optional
import flet as ft
from flet_core import Control
from flet_core.app_bar import AppBar
from flet_core.control import OptionalNumber
from flet_core.floating_action_button import FloatingActionButton
from flet_core.navigation_bar import NavigationBar
from flet_core.types import CrossAxisAlignment, MainAxisAlignment, PaddingValue, ScrollMode

class LoginView(ft.View):
    route = "/"
    
    def __init__(self, page:ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.appbar = ft.AppBar(
            title=ft.Text("Login View"),
            
        )
        
        self.page = page if self.page is None else self.page
        self.username_txt = ft.TextField(helper_text="Username",)
        self.password_txt = ft.TextField(helper_text="Password", password=True, can_reveal_password=True)
        self.success = ft.ElevatedButton("Ingresar", on_click=self.ingresar_click)
        
        self.controls = [
            ft.Container(
                content=ft.Row([
                    self.username_txt,
                    self.password_txt,
                    self.success,
                ])
            )
        ]
    
    def ingresar_click(self, e:ft.ControlEvent):
        if not self.username_txt.value:
            self.username_txt.error_text = "Ingrese nombre"
            self.update()
        elif not self.password_txt.value:
            self.password_txt.error_text = "Ingrese password"
            self.update()
        else:
            self.page.session.set("username", self.username_txt.value)
            self.page.session.set("password", self.password_txt.value)
            self.page.go("/chat")
        
    
    





def main(page: ft.Page):
    page.title = "Routes Example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    
    def route_change(route:str):
        troute = ft.TemplateRoute(page.route)
        page.views.clear()
        page.views.append(
            LoginView(page=page)
        )
        if troute.match("/chat"):
            page.views.append(
                ft.View("/chat", [ft.Text("AAAAAAAAAAA")])
            )
        
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    

    
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)