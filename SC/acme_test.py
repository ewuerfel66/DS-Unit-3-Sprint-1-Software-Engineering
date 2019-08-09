# Imports
import unittest
from acme import Product
from acme_report import generate_products, prefix, suffix

# Test my Product class
class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Test default product weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test that stealability method works fine"""
        prod = Product('Test Product')
        prod.price = 100
        prod.weight = 10
        self.assertEqual(prod.stealability(), "Very stealable!")

# Test my acme_report module
class AcmeReportTests(unittest.TestCase):
    """Ensuring Acme Execs get the best information!"""
    def test_default_num_products(self):
        """Test default length"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test that all generated names are legal"""
        # Find product names
        names = [prod.name for prod in generate_products()]

        for name in names:
            first = name.split()[0]
            last = name.split()[1]
            self.assertIn(first, prefix)
            self.assertIn(last, suffix)    

# Call tests
if __name__ == '__main__':
    unittest.main()