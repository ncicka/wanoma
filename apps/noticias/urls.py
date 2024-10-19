
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    
	path('Editar/<int:pk>', views.Editar_Noticia.as_view(), name = 'editar'),
 
 	path('Agregar', views.Agregar_Noticia.as_view(), name = 'agregar'),
  
  	path('Categoria/', views.Listar_Categoria.as_view(), name = 'categoria'),
   	path('Categoria/Agregar', views.Agregar_Categoria.as_view(), name = 'agregarcategoria'),
    path('Categoria/Editar/<int:pk>', views.Editar_Categoria.as_view(), name = 'editarcategoria'),
    path('Categoria/Borrar/<int:pk>', views.Borrar_Categoria.as_view(), name = 'borrarcategoria'),
	
]