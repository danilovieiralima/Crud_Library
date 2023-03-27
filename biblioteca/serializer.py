from rest_framework import serializers
from biblioteca.models import Livros

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'isbn', 'autor', 'titulo', 'descricao', 'datapub']

  