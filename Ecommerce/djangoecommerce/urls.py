"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.contrib.auth.views import login



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    #url(r'^produto/$', views.product, name='product'),
    #url(r'^produtos/$', views.product_list, name='products'),
   # url(r'^produtos/', include('catalog.urls', namespace='catalog')), #href="{% url 'catalog:product_list' %}"
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
]
