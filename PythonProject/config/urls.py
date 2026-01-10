
from django.contrib import admin
from django.urls import path,include

# Define as configurações de URL para o projeto Django
urlpatterns = [
    # Mapeia a URL 'admin/' para o site de administração do Django
    path('admin/', admin.site.urls),
    # Inclui as URLs do aplicativo 'paginas' na raiz do projeto
    path('',include('paginas.urls')),
]
