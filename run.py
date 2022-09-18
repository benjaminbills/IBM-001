import math
from sales import Sales

basic_tax_exceptions = ['book','food','medical', 'chocolates', 'chocolate','pills' ]

def create_product(product, price):
  product = Sales(product,price)
  return product
  
def save_product(sales):
  sales.save_item()

def display_sales():
  return Sales.display_sales()

def tax_round(tax):
    """ Rounding rule for sales taxes """
    rnd = 20  # How many times 0.05 fits in 1.00? 20.
    return math.ceil(round(tax, 2) * rnd) / rnd

def basic_sales_tax(price):
  return price* .1
  
def import_duty(price):
  return price* .05

def check_basic_tax_exempt(product):
  array_product_name = product.split(' ')
  return any(item in basic_tax_exceptions for item in array_product_name)

def main():
  pass

if __name__ == '__main__':

    main()