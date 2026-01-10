from django.shortcuts import render

# Define uma função chamada 'home' que será a view para a página inicial.
# Esta função recebe um objeto 'request' como argumento, que contém informações sobre a requisição HTTP.
def home(request):
    # A função 'render' é usada para renderizar um template HTML e retornar uma resposta HTTP.
    # O primeiro argumento é o objeto 'request'.
    # O segundo argumento é o caminho para o arquivo de template HTML que será renderizado.
    # Neste caso, ele está procurando por 'index.html' dentro da pasta 'paginas' no diretório de templates.
    return render(request,"paginas/index.html")
