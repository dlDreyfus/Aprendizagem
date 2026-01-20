from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    list_filter = ('data_publicacao',)
    search_fields = ('titulo', 'conteudo')

