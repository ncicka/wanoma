from django.urls import path
from django.views.generic import TemplateView
from .views import ContactoView

app_name = 'contacto'

urlpatterns = [
    path('', ContactoView.as_view(), name='contacto'),
    path('gracias/', TemplateView.as_view(template_name='contacto/gracias.html'), name='gracias'),
]