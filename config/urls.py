from django.contrib import admin
from django.urls import path
from biblioteca import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('livros/', views.LivrosList.as_view()),
    path('livros/<int:pk>/', views.LivrosDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
