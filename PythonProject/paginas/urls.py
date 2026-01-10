from django.urls import path
# Importa o módulo views do diretório atual.
# O módulo views contém as funções que lidam com as requisições HTTP.

from . import views
# Define os padrões de URL para a aplicação 'paginas'.
urlpatterns = [
    # Define um padrão de URL para a raiz ('') da aplicação.
    # Quando a URL for a raiz, a função 'home' do módulo 'views' será chamada.
    # O nome 'home' é usado para referenciar esta URL em templates ou outras partes do código.
    path('', views.home, name='home'),
]