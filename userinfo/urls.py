from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:pk>', views.userPage, name='user-page'),
    path('edit-user', views.editUser, name='edit-user'),
    path('itens-comprados', views.itensComprados, name='itens-comprados'),
    path('anuncios-user', views.anunciosUser, name='anuncios-user')
]
