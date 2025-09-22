# del keyword
# Used to delete object properties or object itself.

from numpy import real
from sklearn.feature_extraction import img_to_graph


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("amol")

# del s1
# print('s1:', s1.name)

class Account:
    def __init__(self, acc_number, acc_password):
        self.acc_number = acc_number
        self.__acc_password = acc_password
    
    def reset_password(self):
        return self.__acc_password

acc1 = Account("123", "abcde")

# print('acc1.acc_number:', acc1.acc_number)
# print(' acc1.acc_password:',  acc1.__acc_password) # this is private, we can not access it outside of Class
# print('reset_password:', acc1.reset_password())

class Person:
    __name = "anonymous"

    def __hello(self, name):
        print("hello")
    
    def welcome(self):
       self.__hello(self)

p1 = Person()
# print('p1:', p1.__name)
# p1.__hello("amol")
# p1.welcome()
# _____________________________________________________________________

# Inheritance
# Base/Parent Class

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

# Child class
class ToyotoCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotoCar):
    def __init__(self, type):
        self.type = type

c1 = ToyotoCar("Fortuner")

c2 = ToyotoCar("prius")

c3 = Fortuner("diesel")

# print('c1:', c1.brand)
# c1.start()
# c1.color

# c3.start()
# _____________________________________________________________________

# Multiple Inheritance

class A:
    varA = "welcome to class A" 

class B:
    varB = "welcome to class B"

class C(A, B):
    varA = "welcome to class B"

# c1 = C()
# print('c1:', c1.varA, c1.varB)

# _____________________________________________________________________

# super

class BaseCar:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("class stopped")

class BaseToyotaCar(BaseCar):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

# car_toyota = BaseToyotaCar("primpus", "diesel")
# print('car_toyota.name:', car_toyota.name, car_toyota.type)
# print('car_toyota.type:', )

# _____________________________________________________________________
# classsmethod

class Person:
    name = "anonymous"
    
    
    # def changeName(self, name):
    #     self.name = name
        # Person.name = name
        # self.__class__.name = name
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

person = Person()
person.changeName("Rahul")
# print('person:', person.name)
# print('Person:', Person.name)

# _____________________________________________________________________
# Polymorphism

class Complex:
    def __init__(self, real, img):
        self. real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i",  self.img, "j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 2)
num1.showNumber()

num2 = Complex(11, 22)
num2.showNumber()

# num3 = num1.add(num2) # <-- with add function
# num3.showNumber()

# num3 = num1 + num2 # <-- with __add__ function
# num3.showNumber()

num3 = num1 - num2 # <-- with __add__ function
num3.showNumber()