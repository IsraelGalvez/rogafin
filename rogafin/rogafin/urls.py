"""
URL configuration for rogafin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# seo
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from apps.core.sitemap import (Sitemap)

sitemaps = {
    'site': Sitemap(
        [
            'home',
        ]
    ),
    'home': Sitemap(['home']),
    'quienesSomos': Sitemap(['quienesSomos']),
    'aboutUs': Sitemap(['aboutUs']),
    'creditoEmpresarial': Sitemap(['creditoEmpresarial']),
    'hipotecario': Sitemap(['hipotecario']),
    'terminosCondiciones': Sitemap(['terminosCondiciones']),
    'prestamoAuto': Sitemap(['prestamoAuto']),
    'asesoriaSeguros': Sitemap(['asesoriaSeguros']),
    'adquisicionVivienda': Sitemap(['adquisicionVivienda']),
    'prestamoConstruccion': Sitemap(['prestamoConstruccion']),
    'refinanciamientoHipotecario': Sitemap(['refinanciamientoHipotecario']),
    'adquisicionTerreno': Sitemap(['adquisicionTerreno']),
    'adquisicionTerrenoConstruccion': Sitemap(['adquisicionTerrenoConstruccion']),
    'preventas': Sitemap(['preventas']),
    'prestamoLiquidez': Sitemap(['prestamoLiquidez']),
    'refinanciamientoHipotecarioLiquidez': Sitemap(['refinanciamientoHipotecarioLiquidez']),
    'prestamoRemodelacion': Sitemap(['prestamoRemodelacion']),
    'creditoAnticipo': Sitemap(['creditoAnticipo']),
    'creditoSimple': Sitemap(['creditoSimple']),
    'creditoRevolvente': Sitemap(['creditoRevolvente']),
    'financiamientoArrendamiento': Sitemap(['financiamientoArrendamiento']),
    'prestamoHipotecarioComercial': Sitemap(['prestamoHipotecarioComercial']),
    'tarjetaCredito': Sitemap(['tarjetaCredito']),
    'adquisicionAuto': Sitemap(['adquisicionAuto']),
    'refinanciamientoPrestamoAuto': Sitemap(['refinanciamientoPrestamoAuto']),
    'adquisicionMoto': Sitemap(['adquisicionMoto']),
    'contacto': Sitemap(['contacto']), 
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('apps.contact.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]