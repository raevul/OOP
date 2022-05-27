import peewee
import connections

class BaseModel(peewee.Model):

    class Meta:
        database = connections.sqlite_db

class Category(BaseModel):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255, null=False)
    description = peewee.TextField(null=True)

    def __str__(self):
        return self.name

class Owner(BaseModel):
    id = peewee.PrimaryKeyField()
    first_name = peewee.CharField(max_length=100)
    surname = peewee.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.surname

class Product(BaseModel):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=255)
    description = peewee.TextField(null=True)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)
    owner = peewee.ForeignKeyField(
        Owner,
        on_delete='cascade',
        on_update='cascade',
        related_name='products'
    )
    category = peewee.ForeignKeyField(
        Category,
        on_delete='cascade',
        on_update='cascade',
        related_name='products'
    )

