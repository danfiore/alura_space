"""
A função desse código é de facilitar o tráfego do envio de 
requisições aos apps incluidos em galeria.

"""

from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name = "index"),
    path('imagem/<int:foto_id>', imagem, name = "imagem"),
    path('buscar', buscar, name="buscar"),
]