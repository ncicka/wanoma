from django import forms

class ContactoForm (forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    mensaje = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
