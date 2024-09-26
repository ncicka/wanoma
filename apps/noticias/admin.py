from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, Noticia

admin.site.register(Categoria)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cuerpo', 'imagen', 'categoria_noticia', 'fecha', 'ver_imagen')

    def ver_imagen(self,obj):
        return format_html('<img src={} width="130" height="100" />',obj.imagen.url)

