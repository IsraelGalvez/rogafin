from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name="contacto"),
]