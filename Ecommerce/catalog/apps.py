# coding:utf-8

from django.apps import AppConfig


class CatalogoConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo' #isso altera o nome da aplicacao la no django admin para CATALOGO
                              #tem que fazer a chamada desse metodo la no __init__.py
