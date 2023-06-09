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
from dataclasses import dataclass

@dataclass
class Product:
    type: str
    name: str
    price: float

@dataclass
class ProductInStore:
    def __init__(self, product: Product, amount = 0):
        self.product = product
        self.amount = amount
        self.pred_price = product.price * 1.3
        self.discount = 0

class ProductStore:

    def __init__(self):
        self.products = list()
        self.income = 0


    def add(self, product, amount):
        if isinstance(product, Product):
            for item in self.products:
                if item.product == product:
                    item.amount = item.amount + amount
                    break
            else:
                self.products.append(ProductInStore(product, amount))
        else:
            raise ValueError('Product is not instance of Product class')

    def set_discount(self, identifier, percent, identifier_type='name'):
        for item in self.products:
            if (identifier_type == 'name' and item.product.name == identifier) or \
                   (identifier_type == 'type' and item.product.type == identifier):
                item.discount = percent

    def sell(self, product_name, amount):
        for item in self.products:
            if item.product.name == product_name:
                if item.amount < amount:
                    raise ValueError('There are not so many products in store')
                else:
                    item.amount = item.amount - amount
                    self.income = self.income + amount * (item.pred_price - item.pred_price * item.discount / 100)
                    break
        else:
            raise ValueError('There is not such product in this store')

    def get_income(self):
        return self.income

    def get_all_products(self):
        all_products = list()
        for item in self.products:
            all_products.append(item.product.name)
        return all_products

    def get_product_info(self, product_name):
        for item in self.products:
            if item.product.name == product_name:
                return (item.product.name, item.amount)
        else:
            raise ValueError(f'There is not product with name {product_name} in this shop')


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Sneakers', 300)

s1 = ProductStore()
s2 = ProductStore()

s1.add(p1, 10)
s1.add(p2, 300)
s1.add(p3, 30)

s2.add(p1, 50)
s2.add(p3, 100)

s1.set_discount('Ramen', 20)

for pr in s1.products:
    print(pr.product.name, pr.amount, pr.discount)

for pr in s2.products:
    print(pr.product.name, pr.amount, pr.discount)

s1.sell('Ramen', 100)

for pr in s1.products:
    print(pr.product.name, pr.amount, pr.discount)

print(s1.get_income())
print(s2.get_all_products())

print(s1.get_product_info('Ramen'))