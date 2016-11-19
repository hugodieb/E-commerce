 # coding=utf8

from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from django.conf import settings
from .forms import ContactForm
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView): #categories foi passado pela chamada no settings
    template_name = 'index.html'#nao mudar template_name - causa erro no django

index = IndexView.as_view()#vem pela chamada da url views.index

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    context = {
            'form': form,
            'success': success
        }
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')
