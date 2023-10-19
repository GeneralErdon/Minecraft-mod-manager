


from src.components.appbar import NavigationAppBar
from src.pages.login_app import LoginPage
from flet import View


def routes_handler(page):
    return {
        "/login": View(
            "/login",
            appbar=NavigationAppBar(page),
            controls=[LoginPage(page)],
            vertical_alignment='center',
            horizontal_alignment='center',
            
            ),
        "/home":View(
            "/home",
            appbar=NavigationAppBar(page),
            controls=[]
        )
    }