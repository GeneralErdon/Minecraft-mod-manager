import flet as ft

class message_types:
    CHAT_MESSAGE:str = "chat_message"
    LOGIN_MESSAGE:str = "login_message"

class Message:
    def __init__(self, user:str, text:str, message_type:str) -> None:
        self.user = user
        self.text = text
        
        assert message_type in [message_types.CHAT_MESSAGE, message_types.LOGIN_MESSAGE]
        
        self.message_type = message_type


def main(page:ft.Page):
    def send_onclick(e:ft.ControlEvent):
        page.pubsub.send_all(Message(
            user=page.session_id, text=new_message.value, message_type=message_types.CHAT_MESSAGE
        ))
        #ChatContainer.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        new_message.focus()
        page.update()
    
    def on_message(message: Message):
        if message.message_type == message_types.CHAT_MESSAGE:
            ChatContainer.controls.append(
                ft.Text(f"{message.user}: {message.text}")
            )
        elif message.message_type == message_types.LOGIN_MESSAGE:
            ChatContainer.controls.append(
                ft.Text(message.text, italic=True, color=ft.colors.GREEN_ACCENT_400, size=12)
            )
        page.update()
    
    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Ingrese un nombre pues"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f"{user_name.value} has joined the chat",
                    message_type=message_types.LOGIN_MESSAGE,
                    )
            )
            page.update()
    
    
    user_name = ft.TextField(label="Enter your username")
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bienvenido"),
        content=ft.Column([user_name], tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end"
    )
    
    
    page.pubsub.subscribe(on_message)
    
    ChatContainer = ft.Column()
    new_message = ft.TextField(on_submit=send_onclick)
    
    page.add(
        ChatContainer,
        ft.Row([
            new_message,
            ft.ElevatedButton("Send", on_click=send_onclick)
        ]),
        
    )
    page.update()


ft.app(main, "Chat App", view=ft.AppView.WEB_BROWSER, host="192.168.3.44", port=8080)