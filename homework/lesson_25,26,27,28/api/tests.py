from django.test import TestCase

from .models import Product


class ProductModelTest(TestCase):
    def test_product_str(self):
        product = Product.objects.create(
            name='Laptop',
            price=3500,
        )

        self.assertEqual(str(product), 'Laptop')
