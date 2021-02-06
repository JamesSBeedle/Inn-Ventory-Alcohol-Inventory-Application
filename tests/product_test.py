import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Landlord", "Draught", 12, 1.23, 3.00, "A Strong Pale Ale", "Timothy Taylors" )


    def test_has_name(self):
        self.assertEqual("Landlord", self.product.name)

    def test_has_category(self):
        self.assertEqual("Draught", self.product.category)

    def test_has_stock(self):
        self.assertEqual(12, self.product.in_stock)

    def test_has_cost(self):
        self.assertEqual(1.23, self.product.cost_price)

    def test_has_price(self):
        self.assertEqual(3.00, self.product.sale_price)

    def test_has_description(self):
        self.assertEqual("A Strong Pale Ale", self.product.description)

    def test_has_supplier(self):
        self.assertEqual("Timothy Taylors", self.product.supplier)