import math
from sales import Sales

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

def main():
  pass

if __name__ == '__main__':

    main()