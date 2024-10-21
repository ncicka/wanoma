from django import forms

class ContactoForm (forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    mensaje = forms.CharField(label='Mensaje',required=True,
                            widget=forms.Textarea(attrs={'placeholder': 'Mensaje...'}))
    email = forms.EmailField(label='Su e-mail',required=True,
                            widget=forms.EmailInput(attrs={'placeholder': 'Su e-mail...'}))
    
