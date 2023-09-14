import flet as ft
import os
import requests as rq

"""
Minecraft id: 432
"""

class Main:
    def __init__(self) -> None:
        self._api_key:str = os.environ.get("CURSEFORGE_API_KEY")
        self._url:str = os.environ.get("CURSEFORGE_BASE_URL")
        self.headers:dict[str,str] = {"x-api-key": self._api_key}
    
    def main(self, page:ft.Page):
        page.title = "Ejemplo de pagina"
        page.window_top = 200
        page.window_left = 200
        
        
        page.update()



ft.app(target=Main().main,port=8550, view=ft.AppView.FLET_APP,)