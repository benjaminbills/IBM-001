import unittest
from sales import Sales

class TestSales(unittest.TestCase):
  def setUp(self):
    self.product_details = Sales('1 book', float(12.49))
  
  def tearDown(self):
    Sales.sales_list = []

  def test_init(self):
    self.assertEqual(self.product_details.product_name,'1 book')
    self.assertEqual(self.product_details.price, 12.49)
  
  def test_save_sales(self):
    self.product_details.save_item()
    product_details_2 = Sales('1 music CD', 14.99)
    product_details_2.save_item()
    self.assertEqual(len(Sales.display_sales()), 2)

if __name__ == '__main__':
    unittest.main()