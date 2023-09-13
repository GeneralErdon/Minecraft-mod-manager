import flet as ft
import random
import requests
from requests import Response

def password_gen(lenght:int):
    chars = "abcdefghijklmnñopqrstuvwxyz1234567890;:_-.ç*^`¨_:¿?'¡!@|"
    chars += chars.upper()
    
    result = ""
    for _ in range(lenght):
        
        result += random.choice(chars)
    
    
    return result


class Main:
    headers = {}
    user = None
    
    
    def main(self, page:ft.Page):
        page.title = "Ejemplo de pagina"
        page.window_top = 200
        page.window_left = 200
        
        
        def process(e:ft.ControlEvent):
            if not txt_username.value:
                txt_username.error_text = "Please enter your name"
                
            elif not txt_pass.value:
                txt_pass.error_text = "Please enter password"
                
            else:
                name = txt_username.value
                passwd = txt_pass.value
                
                response:Response = requests.post(
                    "http://192.168.1.81:8000/login/",
                    {
                        "username": name,
                        "password": passwd
                    },
                )
                if response.status_code == 200:
                    data = response.json()
                    self.headers["Authorization"] = "Bearer %s" % (data["token"])
                    self.user:dict = data["user"]
                    page.route = "/dashboard"
                    
                    page.add(
                            ft.Text(
                            value="Hello %s" % (self.user["username"], )
                            ),
                            ft.Text(
                                value=(data["message"] + f" ruta: {page.route}"),
                            ),
                        )
                    
                elif response.status_code == 400:
                    data = response.json()
                    txt_error.value = data["error"]
                    txt_error.visible = True
                
            
            page.update()
        
        def generar(e:ft.ControlEvent):
            width:int = int(txt_pass_width.value)
            txt_pass.value = password_gen(width or 8)
            page.update()
        
        
        txt_username = ft.TextField(label="Username", color=ft.colors.GREEN)
        txt_pass = ft.TextField(label="Password", color=ft.colors.GREEN)
        txt_pass_width = ft.TextField(label="tamaño password", color=ft.colors.GREEN)
        txt_error = ft.Text(value=None, visible=False, color=ft.colors.RED)
        
        page.add(
            txt_username, 
            txt_pass,
            ft.ElevatedButton("Inicia", on_click=process),
            ft.Row(
                [
                    txt_pass_width,
                ft.ElevatedButton(text="Generar contraseña", on_click=generar)
                ],
                
            ),
            txt_error,
            
            )
        
        
        page.update()



ft.app(target=Main().main,port=8550, view=ft.AppView.FLET_APP,)