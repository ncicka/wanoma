from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

from .models import Usuario

from .forms import RegistroForm, LoginForm, UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'
 

class LoginUsuario(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('home')


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('usuarios:perfil_ok')  # Ajusta el nombre de la URL de éxito

    def get_object(self):
        return self.request.user

def confirmacion(request):

    return render(request, 'usuarios/perfil_confirmacion.html')