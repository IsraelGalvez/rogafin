from django.views.generic.base import TemplateView
from django.shortcuts import render

class ContactPageView(TemplateView):
    template_name = "core/contact.html"