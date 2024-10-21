from django import forms
from django.shortcuts import render
from ckeditor.widgets import CKEditorWidget


from .models import Noticia, Categoria


class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo', 'cuerpo', 'categoria_noticia', 'imagen')
        widgets = {
            'cuerpo': CKEditorWidget(),
            'titulo': forms.TextInput(attrs={'class':'form-control',
                                             'label':'Título'}),
            'categoria_noticia': forms.Select(attrs={'class':'form-control',
                                                     'label':'Categoria'}),
        }
    

#imagen = models.ImageField(upload_to = 'noticias')
#categoria_noticia = forms.ForeignKey(Categoria, on_delete = models.CASCADE)
#fecha = models.DateTimeField(auto_now_add=True)

class FiltrarNoticiaForm(forms.Form):
    ORDEN=[(0,'Sin orden'),(1,'Ascendente'),(2,'Descendente')]
    
    id = forms.ChoiceField(label='Categoria:', required=False,
        widget=forms.Select(attrs={'class':'form-control',
                                   'name': 'id'}))
    fecha_desde= forms.DateField(label='Fecha hasta:', required=False,
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type': 'date'}))    
    fecha_hasta= forms.DateField(label='Fecha hasta:', required=False,
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type': 'date'}))
    orden_antiguedad = forms.ChoiceField(label='Orden Fecha', choices=ORDEN, initial=2,
        widget=forms.Select(attrs={'class': 'form-control'}))
    orden_alfabetico = forms.ChoiceField(label='Orden Alfabetico', choices=ORDEN,
        widget=forms.Select(attrs={'class': 'form-control'})) 

# Formularios para Categorias

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label='Descripción', required=True)
    
    class Meta:
        model = Categoria
        fields = ['nombre',]