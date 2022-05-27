from connections import sqlite_db
from models import (
    Category,
    Product,
    Owner
)

@sqlite_db.atomic()
def add_category(category_name, description):
    category = Category(
    name=category_name, 
    description=description
    )
    category.save()

@sqlite_db.atomic()
def add_owner(first_name, surname):
    owner = Owner.create(
        first_name=first_name,
        surname=surname
    )
    print(owner)

@sqlite_db.atomic()
def add_product(title, body, price):
    category = Category.get(id=1)
    owner = Owner.get(id=1)

    product = Product.create(
        title=title,
        description=body,
        price=price,
        owner=owner,
        category=category
    )
    print(product)

# добавление в базу
# add_category('Hi', 'World')
# add_owner('John', 'Snow')
# add_product(
#     'Iphone', 'Test', 100000
# )

# product = Product.raw(
#     '''SELECT * FROM products;'''
# )
# print(product)
# products = Product.select()
# for product in products:
#     print(product.title)
