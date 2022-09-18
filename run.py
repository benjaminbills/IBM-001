import math
from sales import Sales

def create_product(product, price):
  product = Sales(product,price)
  return product
  
def save_product(sales):
  sales.save_item()

def display_sales():
  return Sales.display_sales()

def main():
  pass

if __name__ == '__main__':

    main()