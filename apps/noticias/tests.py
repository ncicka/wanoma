from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from .models import Noticia, Categoria, Usuario

class CategoriaModelTest(TestCase):
    
    def setUp(self):
        Categoria.objects.create(nombre="categoria1")
    
    def test_titulo_articulo(self):
        categoria = Categoria.objects.get(id=1)
        self.assertEqual(categoria.nombre, "categoria1")
        
class NoticiaViewTest(TestCase):
    
    def setUp(self):
        cat=Categoria.objects.create(nombre="categoria1")
        autor=Usuario.objects.create(username="prueba1",first_name="nombre",last_name="apellido")
        noti=Noticia.objects.create(titulo="Noticia1", cuerpo="Aquí hay algo de contenido de noticia1",
                                    categoria_noticia=cat, autor=autor)
    
    def test_view_url_existe_en_lugar_correcto(self):
        resp = self.client.get('/Noticias/')
        self.assertEqual(resp.status_code, 200)
  
    def test_view_usa_template_correcto(self):
        resp = self.client.get(reverse('noticias:listar'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'noticias/listar.html',)
