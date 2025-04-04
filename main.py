import flet as ft
from views.cadastro_views import CadastroView
from views.home_views import HomeView
from views.login_view import LoginView

def main(page: ft.Page):
    page.title = 'Tela de Login'
    login_view = LoginView(page)
    cadastro_view = CadastroView(page)
    home_view = HomeView(page)

    def route_change(route):
        page.views.clear()
        page.views.append(login_view)
        if page.route == '/home':
            page.views.append(home_view)
        if page.route == '/cadastro':
            page.views.append(cadastro_view)
        page.update()    
    
    page.on_route_change = route_change
    if page.route == None or page.route == '':
        page.go('/login')
    else:
        page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)