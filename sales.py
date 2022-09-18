class Sales:
  sales_list = []
  
  def __init__(self,product_name,price):
    self.product_name = product_name
    self.price = price

  def save_item(self):
    Sales.sales_list.append(self)
    
  @classmethod
  def display_sales(products):
    return products.sales_list