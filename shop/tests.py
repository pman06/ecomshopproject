from django.test import TestCase
from .models import Category, Product
# Create your tests here.

class ShopTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test_Category')
        self.product = Product.objects.create(category=self.category, name='test_product', price=300)

    def test_create_category(self):
        category = Category.objects.get(name=self.category.name)
        self.assertEquals(self.category, category)

    def test_create_product_(self):
        product = Product.objects.get(name=self.product.name)
        self.assertEquals(self.product.category, product.category)
        self.assertEqual(self.product, product)
        self.assertTrue(product.available)
