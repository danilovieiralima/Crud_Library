from django.contrib import admin
from django.urls import path, include
from biblioteca.views import LivrosViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'livros', LivrosViewSets)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
