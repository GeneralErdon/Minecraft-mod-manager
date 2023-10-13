import flet as ft
import os


class message_types:
    CHAT_MESSAGE:str = "chat_message"
    LOGIN_MESSAGE:str = "login_message"

class Message:
    def __init__(self, user:str, text:str, message_type:str) -> None:
        self.user = user
        self.text = text
        
        assert message_type in [message_types.CHAT_MESSAGE, message_types.LOGIN_MESSAGE]
        
        self.message_type = message_type



class ChatMessage(ft.Row):
    def __init__(self, message:Message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vertical_alignment = "start"
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user)),
                color=ft.colors.WHITE,
                bgcolor=ft.colors.AMBER
            ),
            ft.Column(
                [
                    ft.Text(message.user, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5
            ),
        ]
        
    
    def get_initials(self, user_name:str) -> str:
        if user_name is None:
            return "Anon"
        return user_name[:1].capitalize()



def main(page:ft.Page):
    page.title = "Flet Chat"
    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Ingrese un nombre pues"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            #modal.open = False
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f"{user_name.value} has joined the chat",
                    message_type=message_types.LOGIN_MESSAGE,
                    )
            )
            page.update()
    
    user_name = ft.TextField(label="Enter your username")
    
    def send_message_click(e:ft.ControlEvent):
        page.pubsub.send_all(Message(
            user=page.session.get("user_name"), text=new_message.value, message_type=message_types.CHAT_MESSAGE
        ))
        #ChatContainer.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        new_message.focus()
        page.update()
    
    def on_message(message: Message):
        if message.message_type == message_types.CHAT_MESSAGE:
            msg = ChatMessage(message)
        elif message.message_type == message_types.LOGIN_MESSAGE:
            msg = ft.Text(message.text, italic=True, color=ft.colors.GREEN_ACCENT_400, size=12)
        
        ChatContainer.controls.append(msg)
        page.update()
    
    
    
    
    
    page.pubsub.subscribe(on_message)
    
    
    ChatContainer = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    new_message = ft.TextField(
        on_submit=send_message_click,
        autofocus=True,
        hint_text="Write message...",
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        )
    
    
    
    page.add(
        ft.Container(
            content=ChatContainer,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True
        ),
        ft.Row([
            new_message,
            ft.IconButton(
                icon=ft.icons.SEND_ROUNDED,
                tooltip="Send",
                on_click=send_message_click,
            )
        ]),
        
    )
    
    
    #page.dialog = modal
    
    #page.update()


ft.app(main, "Chat App", view=ft.AppView.WEB_BROWSER, host="192.168.3.44", port=8080)