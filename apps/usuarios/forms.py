from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    username=forms.CharField(label='Nombre usuario', required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({'class' : 'form-control','placeholder' : "Nombre de usuario", 'type' : 'text'})
        self.fields["password"].widget.attrs.update({'class' : 'form-control','placeholder' : "Contraseña", 'type' : 'text'})

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name', 'last_name','email',]
