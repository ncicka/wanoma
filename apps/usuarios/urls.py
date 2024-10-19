from django.urls import path

from . import views
from .views import UsuarioUpdateView, LoginUsuario


app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    #path('login/', LoginUsuario.as_view(), name='login'),
    path('editar/', UsuarioUpdateView.as_view(), name='editar'),  
    path('confirmacion/', views.confirmacion, name='perfil_ok'),
]