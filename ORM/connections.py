import os
from peewee import SqliteDatabase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sqlite_db = SqliteDatabase (BASE_DIR + '/' + 'db.sqlite3')
