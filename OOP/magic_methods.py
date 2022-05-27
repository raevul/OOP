"""task1"""
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан')

#     def __repr__(self):
#         return f'{self.name} {self.balance}'

#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'
    
#     def __del__(self):
#         print('Пока')

# obj_account = Account('Rick', 2013, 'Bishkek')
# print(obj_account)
# print(repr(obj_account))

"""task2"""
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, num):
#         return f"Это сложение и результат равен: {self.value + num}"

#     def __sub__(self, num):
#         return f'Это вычитание и результат равен: {self.value - num}'

#     def __mul__(self, num):
#         return f'Это умножение и результат равен: {self.value * num}'

#     def __truediv__(self, num):
#         return f'Это деление и результат равен: {self.value / num}'

# obj_int = MyNumber(5)
# print(obj_int + 5)
# print(obj_int - 5)
# print(obj_int * 5)
# print(obj_int / 5)

"""task3"""
# class MyList(list):
#     def __init__(self, mylist):
#         self.mylist = mylist

#     def __getitem__(self, index):
#         return self.mylist[index-1]

# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])

"""task4"""
# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
    
#     def __gt__(self, other):
#         return f'> {sum(self.ball.values())/2 > sum(other.ball.values())/2}'
#     def __lt__(self, other):
#         return f'< {sum(self.ball.values())/2 < sum(other.ball.values())/2}'
#     def __ge__(self, other):
#         return f'>= {sum(self.ball.values())/2 >= sum(other.ball.values())/2}'
#     def __le__(self, other):
#         return f'<= {sum(self.ball.values())/2 <= sum(other.ball.values())/2}'
        
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})

# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2) 

"""task5"""
# class Word:
#     def __init__ (self, string) -> bool:
#         self.string = string.replace(' ', '')

#     def __gt__(self, other) -> bool:
#         return len(self.string) > len(other.string)

#     def __lt__(self, other) -> bool:
#         return len(self.string) < len(other.string)

#     def __ge__(self, other) -> bool:
#         return len(self.string) >= len(other.string)

#     def __le__(self, other):
#         return len(self.string) <= len(other.string)

# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')  
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2)

"""task6"""
# class Kopilka:
#     __total = 0
#     __coins = []

#     def __init__(self):
#         Kopilka.__total = 0
#         Kopilka.__coins = []

#     def add_moneta(self, moneta):
#         Kopilka.__total += moneta
#         Kopilka.__coins.append(moneta)
        
#     def __len__(self):
#         return len(self.__coins)

#     def __getitem__(self, key):
#         res = self.__coins[key]
#         return res
        
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)

# print(len(obj))
# for i in obj:
#     print(i) 

"""task7"""
# class Anagram(str):
#     def __init__(self, string):
#         self.string = string

#     def __eq__(self, other):
#         return self.string == other.string[::-1]

#     def __mul__(self, other):
#         return self.string[::-1] * other

# word1 = Anagram('hello')
# word2 = Anagram('olleh')
# print(word1 == word2)
# print(word1 * 3)
