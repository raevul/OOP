"""Введение в ООП"""
"""task1"""
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         print(f'Название этой песни {self.author}')

#     def show_title(self):
#         print(f'Автор этой песни {self.title}')

#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')


# song = Song('Singer', 'Song', 2000)

# song.show_title()
# song.show_author()
# song.show_year()

"""-----------------------------------------"""
# class Song:

#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         print('Название этой песни', self.title)
    
#     def show_author(self):
#         print('Автор этой песни', self.author)

#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')

# song = Song('Happy', 'Pharrell Williams', '2013')

# song.show_author()
# song.show_title()
# song.show_year()

"""task2"""
# class Circle:
#     color = 'Синий'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return self.pi * self.radius ** 2

# circle = Circle(2)
# circle.color = 'red'                     # переопределение 
# circle.get_area()

"""task3"""
# class BankAccount:
#     balance = 0
#     def __init__(self):
#         BankAccount.balance = 0

#     def withdraw(self, amount):
#         BankAccount.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
    
#     def deposit(self, amount):
#         BankAccount.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

"""task4"""
# class Taxi:
    
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
    
#     def get_total_cost(self, km):
#         self.km = km * self.cost
#         return f'Такси {self.name}, стоимость поездки: {self.km} сом'

# taxi1 = Taxi('Namba', 10, 0)
# taxi2 = Taxi('Yandex', 10, 0)
# taxi3 = Taxi('Jorgo', 10, 0)    

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))
# ------------------------------------------
# class Taxi:

#     def __init__(self,  name, cost, cost_km ):
#        self.name = name
#        self.cost = cost
#        self.cost_km = cost_km

#     def get_total_cost(self, km):
#         b = self.cost + self.cost_km * km
#         return f'Такси {self.name}, стоимость поездки: {b} сом'

# taxi1 = Taxi('Namba', 45, 12)
# taxi2 = Taxi('Jorgo', 46, 13)
# taxi3 = Taxi('Yandex', 50, 14)

# print(taxi1.get_total_cost(5))

# print(taxi2.get_total_cost(6))

# print(taxi3.get_total_cost(7))

"""task5"""
# class Phone:
    
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()

"""task6"""
# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         try:
#             res = self.salary * self.experience * (self.percent/100)
#             return res
#         except:
#             return 0.0

# obj = Salary(10000, 10)
# print(obj.count_percent()) 

"""task7"""
# from datetime import datetime
# class Nobel:
#     def __init__(self, category, year, winner):
#       self.category = category
#       self.year = year
#       self.winner = winner

#     def get_year(self):
#         time = int(datetime.now().year) 
#         return f'выиграл {time - self.year} лет назад'


# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())
  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

"""task8"""
# class Password:
    
#     def validate(self, password):
#         if len(password) < 15 and len(password) > 8:
#             return password
#             if password.isalpha():
#                 return password
#             else:
#                 print('Password should contain numbers too')
#         else:
#             print('Password should be longer than 8, and less than 15')
    
"""task9"""
# class Math:
#     def __init__(self, value):
#         self.value = value

#     def get_factorial(self):
#         if self == 0:
#             return 1
        
 

#     def get_sum(self):
#         return value += 1

#     def get_mul_table(self):
        

# obj = Math(11)
# obj.get_factorial()
# obj.get_sum()
# obj.get_mul_table()

"""task10"""
# class ToDo:
#     instances = {}
#     def __init__(self, **kwargs):
#         pass

#     def give_priority(self, priority):
#         instances.update(priority)








""" Наследование """
"""task1"""
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
    
# class Class2(Class1):
#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())

"""task2"""
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):

#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

"""task3"""
# class MyString(str):

#     def __init__(self, string):
#         self.string = string

#     def append(self, string):
#         return self.string
        
#     def pop(self):
#         return self.string
        
        
# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop())
# print(example)



"""Полиморфизм"""
"""task1"""
# a = 'hello'
# b = [1, 2, 3]
# c = {1: 'first', 2: 'second'}

# d = [a, b, c]
# for i in d:
#     print(len(i))

"""task2"""
# class Dog:
#     def voice(self):
#         print('Гав')
    
# class Cat:
#     def voice(self):
#         print('Мяу')

# def to_pet(animal):
#     animal.voice()

# rex = Dog()
# barsik = Cat()
# to_pet(barsik)
# to_pet(rex)

"""task3"""
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'{super().get_info()}, я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'{super().get_info()}, я учусь в {self.university} на {self.course} курсе'

# person = Person('Nurka', 'Tur')
# employee = Employee('Nurka', 'Tur', 'Google', 'Senior')
# student = Student('Nurka', 'Tur', 'DrexelU', '1')

# def get_human_info(x):
#     print(x.get_info())
    
# get_human_info(person) 
# get_human_info(employee) 
# get_human_info(student)

"""task4"""


"""Инкапсуляция"""
"""task1"""
# class A:
#     def public(self):
#         return 'Public method'
#     def _protected(self):
#         return 'Protected method'
#     def __private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

"""task2"""
# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass

# b1 = B()
# b1.method1()

"""task3"""
# class Car:
#     def __init__(self):
#         self.__speed = 0

#     def set_speed(self, new):
#         self.__speed = new

#     def show_speed(self):
#         return self.__speed
    
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 

"""task4"""
# class Car:
#     def __init__(self):
#         self.__speed = 0

#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, new):
#         self.__speed = new

# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 


"""Множественное наследование, миксины"""
"""task1"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()

"""task2"""
# class RadioMixin:
#     def play_music(self):
#         title = 'Lose Youself'
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     def ride(self, title):
#         print(f'Песня называется {title}')

# class Boat(RadioMixin):
#      def swim(self, title):
#         print(f'Песня называется {title}')

# class Amphibian(Auto, Boat):
#     pass

# auto = Auto()
# auto.play_music()
# boat = Boat()
# boat.play_music()
# obj = Amphibian()
# obj.play_music()

"""task3"""
# import time
# class Clock:
#     def current_time(self):
#         self.time = time.strftime('%H:%M:%S')
#         print(self.time)

# class Alarm:
#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         print('Будильник отключен')
    
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()
# ==========================
# class Clock:
#     def current_time(self):
#         import datetime
#         now = datetime.datetime.now()
#         print(now.strftime('%H:%M:%S'))

# class Alarm:
#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         print('Будильник отключен')
    
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

class Word:
    def __new__(self, wor):
        self.wor = wor.replace(' ', '')
        print(self.wor)

obj = Word('h e l l o')
print(obj)
