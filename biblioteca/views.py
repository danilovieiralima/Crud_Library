from rest_framework import viewsets
from biblioteca.models import Livros
from biblioteca.serializer import LivrosSerializer
from rest_framework import renderers


class LivrosViewSets(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
