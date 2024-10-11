from django import forms
from django.shortcuts import render
from ckeditor.widgets import CKEditorWidget


from .models import Noticia, Categoria


class EditarNoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo', 'cuerpo', 'categoria_noticia')
        widgets = {
            'cuerpo': CKEditorWidget()
        }
    

#imagen = models.ImageField(upload_to = 'noticias')
#categoria_noticia = forms.ForeignKey(Categoria, on_delete = models.CASCADE)
#fecha = models.DateTimeField(auto_now_add=True)
