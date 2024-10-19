from django.core.mail import send_mail
from django.conf import settings

from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from .forms import ContactoForm

# Create your views here.

class ContactoView(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto:gracias')  # Ajusta a tu URL de éxito

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']
        
        full_message = f"""
            Recibido el siguiente mensaje de  {email}, {nombre}
            ________________________


            {mensaje}
            """
        send_mail(
            subject=f'Mensaje de {nombre}',
            message= full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        return super().form_valid(form)

