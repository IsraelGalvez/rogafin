from django.views.generic.edit import FormView
from . forms import ContactForm

class ContactPageView(FormView):

    template_name = "contact/contact.html"
    success_url = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
