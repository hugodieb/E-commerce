from  django.test import TestCase, Client
from model_mommy import mommy
from django.core.urlresolvers import reverse
from catalog.models import Category, Product

class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')# testa a url catalogo/
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)# cria 10 produtos na tabela produtos

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/products_list.html')# verifica se retorna o template

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)# verifica se existe o context carregado
        product_list = response.context['products']# carrega os produtos do contexto
        self.assertEqual(product_list.count(), 3)# verifica se tem 10 produtos que foram criado la em cima.
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4)

    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404)