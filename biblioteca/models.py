from django.db import models

class Livros(models.Model):
    isbn = models.CharField(max_length=13)
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    datapub = models.DateField()
    
    def __str__(self):
        return self.titulo
    