from django.contrib import admin
from biblioteca.models import Livros

class Livro(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'autor','titulo','descricao','datapub')
    list_display_links = ('id', 'autor', 'titulo')
    search_fields = ('titulo',)
    
admin.site.register(Livros, Livro)
