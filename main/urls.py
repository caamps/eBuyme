from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar-anuncio/', views.criarAnuncio, name='criar-anuncio'),
    path('anuncio/<str:pk>/', views.anuncioView, name='anuncio'),
    path('anuncios/', views.listaAnuncios, name='lista-anuncios'),
    path('lista_categorias', views.listaCategorias, name='lista-categorias'),
    path('carrinho/', views.carrinhoView, name='carrinho'),
    path('delete-anuncio/<str:pk>', views.deleteAnuncio, name='delete-anuncio'),
    path('finalizar-compra/', views.finalizarCompra, name='finalizar-compra'),
]
