# Task 3
#
# Product Store
#
# Write a class Product that has three attributes:
#
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
# additional classes to operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
#
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by
# input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
# ```

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def add(self, product, amount):
        product.amount = amount
        product.pred_price = product.price * 1.3

    def set_discount(self, identifier, percent, identifier_type='name'):

        pass

    def sell(self, product_name, amount):
        self.product_name

    def get_income(self):
        pass

    def get_all_products(self):
        pass

    def get_product_info(self, product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.add(p, 30)

print(p.amount)
# s.sell('Ramen', 10)

# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
