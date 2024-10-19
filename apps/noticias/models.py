from django.db import models
from apps.usuarios.models import Usuario
from ckeditor.fields import RichTextField

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150, verbose_name='Título')
	#cuerpo = models.TextField(verbose_name='Texto de la noticia')
	cuerpo = RichTextField(verbose_name='Texto de la noticia')
	imagen = models.ImageField(upload_to = 'noticias', verbose_name='Imagen')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	autor = models.ForeignKey(Usuario, on_delete = models.CASCADE, default=1)

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.noticia}->{self.texto}"