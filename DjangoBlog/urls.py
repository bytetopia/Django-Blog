"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^manager/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),
    url(r'^ads.txt$', RedirectView.as_view(url=r'static/ads/ads.txt')),
    url(r'^bdunion.txt$', RedirectView.as_view(url=r'static/ads/bdunion.txt')),
    url(r'^search/', include('haystack.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
