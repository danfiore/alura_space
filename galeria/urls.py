"""
A função desse código é de facilitar o tráfego do envio de 
requisições aos apps incluidos em galeria.

"""

from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name = "index"),
    path('imagem/', imagem, name = "imagem")
]