from django.views.generic.edit import FormView
from . forms import ContactForm
from . functions import send_email
from django.urls import reverse_lazy
from django.contrib import messages

class ContactPageView(FormView):

    template_name = "contact/contact.html"
    success_url = reverse_lazy('contacto')
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phoneNum = form.cleaned_data['phoneNum']
        credit_interest = form.cleaned_data['credit_interest']
        credit_interest_display = form.cleaned_data['credit_interest']
        credit_interest_label = dict(form.fields['credit_interest'].choices)[credit_interest_display]
        message = form.cleaned_data['message']
        mensaje = f'Nombre: {name}\nCorreo: {email}\nTeléfono: {phoneNum}\nCrédito de interés: {credit_interest_label}\nMensaje: {message}'
        send_email(name, email, mensaje)
        messages.success(self.request, 'Tu mensaje ha sido enviado correctamente.')
        return super().form_valid(form)