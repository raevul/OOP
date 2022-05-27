""" инициализация --> создать """
# print(dir(object))

"""
наследования - class Person(object) --> object - наследование
инкапсуляция - андерскоры  _ , __ --> одна задача в одном классе есть все необходимые методы для решения этой задачи
полиморфизм - одинаковые методы, но выполняют разные функции
"""

"""
+ --> __add__ 
== --> __eq__
"""



# class Person:
#     legs = 2
#     arms = 2
#     eyes = 2
#     mouth = 1


#     def __init__(self, name, age):           # self -> это объект, ссылка на объект   init -> инициализация объкта, создание
#         self.name = name
#         self._age = age
#         self.__secret = 'secret'

#     def walk(self, km):
#         print(f'{self.name} ходит {km} км')

#     def __str__(self):
#         return f"{self.name} - {self._age}"


# person1 = Person('Nastya', 18)
# print(str(person1))

# person1 = Person('Nastya', 18)         # объект
# person2 = Person('Ular', 20)
# print(dir(person1))
# print(person1.name)
# print(person1._age)
# print(person1._Person__secret)

# person1.walk(2)
# person2.walk(3)


"""отличие функции от метода в том что метод принимает объект"""




# class Person:
#     def __init__(self, name, age, sex) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.is_run = False
#         self.is_speak = False
#         self.is_go = False

#     def speak(self):
#         if self.age > 5:
#             self.is_speak = True
#         if self.is_speak:
#             print('Run successfully')
#         else:
#             print('I can\'t run')


#     def go(self):
#         if self.age > 5:
#             self.is_go = True
#         if self.is_go:
#             print('Speak successfully')
#         else:
#             print("I can't speak")


#     def run(self):
#         if self.age > 5:
#             self.is_run = True
#         if self.is_run:
#             print('Go successfully')
#         else:
#             print("I can't go")

# John =  Person(name='John', age=6, sex='male')
# John.speak()
# John.run()
# John.go()





# class Student:
#     def __init__(self, first_name, last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.books = []
#         self.knowledge = 0
#         self.is_ready_to_work = False
#         self.languages = {}

#     def read_book(self, book_title):
#         self.books.append(book_title)
#         self.__add_points(100)

#     def do_homework(self):
#         self.__add_points(10)

#     def do_real_world_project(self):
#         self.__add_points(50)

#     def __add_points(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             print('This student if ready to work')
#             self.is_ready_to_work = True

#     def learn_new_language(self, name_of_language, number):
#         if number < 1 or number > 100:
#             raise ValueError('Invalid number')
#         self.languages[name_of_language] = number



# stl = Student('John', 'Connor')                            d # создаем экземпляр класса Student
# print(f'Количество баллов у {stl.first_name}: ', stl.knowledge)
# stl.read_book('Terminator1')
# stl.read_book('Чингиз Айтматов - Первый учитель')
# stl.read_book('Jack London - Морской волк')
# stl.read_book('Марк Лутц - Python3')
# stl.do_homework()
# stl.do_real_world_project()
# stl.do_real_world_project()

# stl.learn_new_language('Python3', 10)
# stl.learn_new_language('Морской волк', 5)
# print(stl.books)
# print(stl.languages)
# print(f'Количество баллов у {stl.first_name}: ', stl.knowledge)




# self - сам объект 
# __init__ - инициализатор устанавливает доп параметры


""" Наследование """

# create, read(get), update, delete

# class BaseCrud:
#     def __init__(self) -> None:
#         self.data = []
#         self.id_ = 1
    
#     def get(self, number_id):
#         for d in self.data:
#             if d.get(number_id):
#                 return d
#         else:
#             return None

#     def create(self, data: dict):
#         self.data.append({self.id_: data})
#         self.id_ += 1

#     def update(self, number_id, data: dict):
#         pass

#     def delete(self, number_id):
#         for d in self.data:
#             if d[number_id]:
#                 self.data.remove(d)


# class Book(BaseCrud):                     # класс Book наследуется от класса BaseCrud
#     pass


# book = Book()
# print("Before call method create: ", book.data)
# book.create({'name': 'Python3'})
# book.create({'name': 'Python3'})
# print("After call method create: ", book.data)
# print("Searched: ", book.get(1))
# print(book.get(1))



# class A:
#     pass

# a = A()      # а -> это объект(object)(экземпляр(instance)) класса A, чтобы удостоверится есть метод isinstance( a (объект класса), A (tuple) )
# print(isinstance(a, A))  -> True or False

# class Dog:
#     # name = 'Rex'              
#     # age = 3             # name и age являются атрибутами класса Dog или свойства
#     owner = 'John'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age              # создаем атрибут

#     def __str__(self):
#         return f'{self.name} {self.age}'

#     def bark(self):
#         print('gav-gav')

#     def dog_info(self):
#         return f'This is {self.name}, he is {self.age} years old'

#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         return f'{self.name} is {self.age} now'

#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self



# dog1 = Dog(name='Rex', age=3)         #  dog1 -> это экземпляр класса Dog
# dog2 = Dog(name='Bobik', age=2)
# dog3 = Dog(name='Oreo', age=1)
# dog1.friends(dog2)
# print(dog1.friend)  # print(dog2)
# print(dog2.friend)
# dog1.bark()
# dog2.bark()
# dog3.bark()
# print(dog1)
# print(dog2.dog_info())
# print(dog1.birthday('strawberry'))
# print(dog2.birthday('vanilla'))
# print(dog3.birthday('choclate'))
# print(dog1.cake)
# print(dog2.cake)
# print(dog3.cake)
# print(dog1.age)

# dog3.owner = 'Alice'
# print(dog1.name)
# print(dog2.name)
# dog1.name = 'Tuzik'
# print(dog1.name)
# dog1.food = 'meat'           # можно создавать атрибуты на ходу
# print(dog1.food)
# print(dog1.owner)
# print(dog2.owner)
# print(dog3.owner)



# class Rectangle:
    
#     default_color = 'red'

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         return self.width * self.length

# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2, 7)
# # print(rec1.area())
# # print(rec1.width)
# # print(rec2.length)
# # print(rec2.area())
# rec2.default_color = 'yellow'
# print(rec1.default_color)
# print(rec2.default_color)


# class Car:

#     car_count = 0

#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.car_count)



"""ООП - парадигма"""

"""Основные"""
# 1. Наследование - это принцип ООП
# 1.2 Множественное наследование
# 2. Полиморфизм
# 3. Инкапсуляция

"""Дополнительные"""
# 1. Абстракция
# 2. Ассоциация
# 2.1. Агрегация
# 2.2. Композиция




"""Наследование -> принцип ООП, где мы можем в дочернем классе унаследовать, переопределять и использовать все методы и аттрибуты родительского класса"""
# class A:
#     def method1(self):
#         """Этот метод выводит строку"""
#         print('method1 in class A')
    
# class B(A):
#     """Наследовали все методы и аттрибуты у класса А"""

# b = B()         # создали объект (экземпляр) от класса B
# b.method1()     # Можем вызвать метод method1, который был создан в классе A



"""Полиморфизм -> принцип ООП, где мы можем создавать в разных классах одноименные методы и аттрибуты с разным функционалом"""
# class A:
#     def __str__(self) -> str:
#         """
#         Метод __str__ работает когда :
#         1. Мы оборачиваем объект в str -> str(A())
#         2. Принтим объект -> print(A())
#         """
#         return 'A object'

# class B:
#     def __str__(self):
#         return 'B object'

# print(A())   # A object
# print(B())   # B object



"""Инкапсуляция -> принцип ООП, где мы можем делать аттрибуты и методы с разным уровнем доступа"""
# class A:
#     attribute1 = 'публичный аттрибут'
#     _attribute2 = 'защищенный аттрибут'
#     __attribute3 = 'приватный аттрибут (но можно обратиться так: _A__attribute3)'

#     def method1(self):
#         return 'публичный метод'
    
#     def _method2(self):
#         return 'защищенный метод'
    
#     def __method3(self):
#         self.__attribute3
#         return 'приватный метод (_A__method3)'

# A().__attribute3 -> AttributeError
# A()._A__attribute3 -> "приватный аттрибут (но можно обратиться так: _A__attribute3)"

"""Getters and Setters"""
# это методы, через которые мы можем получать(getter) и изменять значения защищенных и приватных аттрибутов.
# class A:
#     _attr1 = 'защищенный аттрибут'
#     __attr2 = 'приватный аттрибут'

#     def get_attr1(self):
#         """возвращает значение аттрибута _attr1"""
#         return self._attr1

#     def get_attr2(self):
#         """возвращает значение аттрибута __attr2"""
#         return self.__attr2

#     def set_attr1(self, value):
#         """меняет значение _attr1"""
#         self._attr1 = value

#     def set_attr2(self, value):
#         """меняет значение __attr2"""
#         self.__attr2 = value

# a = A()
# print(a.get_attr1(), a.get_attr2())
# a.set_attr1('New val')
# a.set_attr2('Val')
# print(a.get_attr1(), a.get_attr2())


"""Множественное наследование - принцип ООП, в котором мы наследуем все аттрибуты и методы у всех родителей"""
# class A:
#     def method_a(self):
#         ...

# class B:
#     def method_b(self):
#         ...

# class C(A,B):
#     """Класс унаследовал все аттрибуты и методы класса А и класса В и все аттрибуты и методы их родителей (object)"""

# c = C()
# c.method_a()
# c.method_b()


"""проблемы множественного наследования"""
# 1. Проблема ромба (решена через mro)
# 2. Проблема перекрестного наследования (не решена)

"""проблема ромба"""
# class A:
#     """корневой класс"""

#     def method_a(self):
#         return 'A'

# class B(A):
#     """первый дочерный класс от А"""

#     def method_b(self):
#         return 'B'

# class C(A):
#     """второй дочерный класс от А"""

#     def method_c(self):
#         return 'C'

# class D(B, C):
#     """дочерный класс от В и С"""

#     def method_d(self):
#         return 'D'


# d = D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()
# print(D.mro())
# print(D.__mro__)
# print(dir(object.__class__))

# MRO - D -> B -> C -> A

"""проблема перекрестного наследования"""
# class A:
#     ...
# class B:
#     ...
# class C(A, B): ...
# class D(B, A): ...

# class E(C, D): ... -> TypeError









""" Mixins - примеси """

# В конце название хранить Mixin
# PostMixin

# Не должен хранить состояние (например __init__)


# class CreateMixin:
#     def create(self):
#         print('Create')

# class UpdateMixin:
#     def update(self):
#         print('Update')

# class DeleteMixin:
#     def delete(self):
#         print('Delete')

# class Restoran(CreateMixin, UpdateMixin, DeleteMixin):
#     def __init__(self, name, address):
#         self.name = name 
#         self.address = address

#     # def create_restoran(self):
#     #     self.create()

# restoran1 = Restoran('Freshbox', 'Isanova')
# restoran1.create()
# restoran1.delete()
# restoran1.update()



# class LoginRequiredMixin:   -> для класса
#     pass


# @login_required    -> для функции


# users = {
#     "user1": 123,
#     "user2": 321
# }

# def login_required(func):
#     def wrapper(user):
#         if user not in users.values():
#             raise AuthenticationError('User is not Authenticated')
        
#         func(user)
#         print('Успешно авторизован')
#         return

#     return wrapper


# @login_required
# def some_page(user):
#     pass

# some_page(123435)



# from multiprocessing import AuthenticationError


# class View:
#     def __init__(self) -> None:
#         self.users = ['John', 'Raychel']

#     # def dispatch(self):
#     #     print('Метод диспатч')
#     #     self.users


# class LoginRequiredMixin:
#     def dispatch(self, request, user):
#         if user not in self.users:
#             raise AuthenticationError('User is not authenticated')
#         return self.users

# class AboutPage(View, LoginRequiredMixin):
#     pass

# obj = AboutPage()
# obj.dispatch('test', 'John')




"""
instance -> объект -> экземпляр класса
self -> ссылка на самого себя
"""




"""check myself"""
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} тип кухни {self.cuisine_type}')

#     def open_restaurant(self):
#         print('Ресторан открыт')



# restaurant1 = Restaurant('Istanbul', 'Turkish')
# restaurant2 = Restaurant('Navat', 'National')
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant1.open_restaurant()



# class User:
#     def __init__(self, first_name, last_name, age, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email

#     def descride_user(self):
#         print(f'{self.first_name} {self.last_name} {self.age} {self.email}')

#     def greet_user(self):
#         print(f'Здравстуйте {self.first_name} {self.last_name}')

# user1 = User('Улар', 'Раев', 20, 'ular@gmail.com')
# user2 = User('John', 'Snow', 21, 'john@gmail.com')
# user1.descride_user()
# user1.greet_user()
# user2.descride_user()
# user2.greet_user()



# class User:
#     count = 0
#     def __init__(self, name, last_name, age, email, password):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.password = password

#     def input_(self):
#         print(f'{self.name}')
#         print(f'{self.last_name}')
#         print(f'{self.age}')
#         print(f'{self.email}')
#         print(f'{self.password}')

#     def sum_input(self):
#         count += 1
        



# class Solder:
#     def __init__(self, id, team):
#         self.id = id
#         self.team = team

#     def go_hero(self, id):
#         print(f'Иду за героем {id}')
            
# class Hero:
#     level = 0
#     def __init__(self, id, team):
#         self.id = id
#         self.team = team

#     def level_up(self):
#         Hero.level += 1


# hero1 = Solder(1, 'Blue')
# hero2 = Hero(2, 'Red')
# hero1.go_hero(1)
# hero2.level_up()
# obj1 = []
# obj2 = []
# for i in range(1, 10):
#         obj1.append(i)
#         obj2.append(i)
#         if len(obj1) > len(obj2):
#             print(f'Первый герой победил у него: {len(obj1)} солдат')
#         elif len(obj1) < len(obj2):
#             print(f'Второй герой победил у него: {len(obj2)} солдат')
#         else:
#             print('Количество солдат одинаковое!')