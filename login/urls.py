from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', views.logoutView, name='logout'),
    path('ativar/<uidb64>/<token>', views.ativarView, name='ativar'),
    path('alterar-senha/<uidb64>/<token>', views.trocarView, name='alterar-senha'),
    path('requerir-troca/', views.requerirTroca, name='requerir-troca')
]

