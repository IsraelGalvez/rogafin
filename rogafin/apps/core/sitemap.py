from django.contrib.sitemaps import Sitemap # Importamos la clase Sitemap
from datetime import datetime
from django.urls import reverse_lazy # Importamos datetime y timedelta

    
class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changeFreq(self, obj):
        return 'never'
    
    def lastmod(self, obj):
        return datetime.now()
    
    def location(self, obj):
        return reverse_lazy(obj)