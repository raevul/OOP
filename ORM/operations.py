import peewee
from connections import sqlite_db
from models import Category, Owner, Product


try:
    with sqlite_db.atomic():
        sqlite_db.create_tables([Category, Owner, Product])
except Exception as e:
    print(e)
    