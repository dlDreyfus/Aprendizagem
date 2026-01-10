from django.db import models

# Define o modelo Artigo que herda de models.Model
class Artigo(models.Model):
    # Campo para o título do artigo, com um limite de 200 caracteres
    titulo = models.CharField(max_length=200)
    # Campo para a data e hora de criação do artigo, preenchido automaticamente na criação
    criado_em = models.DateTimeField(auto_now_add=True)

    # Método que define a representação em string de um objeto Artigo
    # Retorna o título do artigo
    def __str__(self):
        return self.titulo