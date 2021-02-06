import unittest
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("Timothy Taylors", "Knowle Spring Brewery, Queens Road, Keighley", "01535605506", "Landlord" )

    
    def test_has_name(self):
        self.assertEqual("Timothy Taylors", self.supplier.name)

    def test_has_address(self):
        self.assertEqual("Knowle Spring Brewery, Queens Road, Keighley", self.supplier.address)

    def test_has_phone_number(self):
        self.assertEqual("01535605506", self.supplier.phone_number)

    
    def test_has_product(self):
        self.assertEqual("Landlord", self.supplier.product)