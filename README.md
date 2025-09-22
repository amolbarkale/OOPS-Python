# OOPS-Python

functions - reduce redundancy and increase reusability

Object Oriented Programming (OOP) - Similar for OOP also

It is not necessary to use always functional programming or OOPS principles, it depends upon usecase and application LLD

## Object - 
We dont directly create objects, first we create class then create objects in codeing.
Ex. List, String etc are objects in Python

## `Class` - 
Class is a blueprint for creating objects .

## Constructor -
All classes have a function called __init__(), which is always executes when the class is being initiated.

## `self` - 
The self param is a reference to the current instance of the class, and is used to access variables that belongs to the class

## `Class` and Instance Attributes - 
Class.attr - common attribute for all Classes
obj.att - different attributes for all Class instances

## Methods -
Methods are function that belongs to objects

## Static Methods `staticmethod` -
methods that does not depends upon objects, thay are always static

## 4 Pillars of OOP - 
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

## Abstraction -
Hiding the implementation details of a class only showing the essential feature to the user.

## Encapsulation - 
Wrapping data and funfciotns into a single unit (Object)

## `del` keyword
Used to delete object properties or object itself.

## Private(like) attributes and methods
Conceptual Implementations in Python

Private attr and methods are meants to be used only within the class and are not accessible from outside the class

## Inheritance
When one class (child/derived) derives the properties and methods of another class(parent/base)

1. Single inheritance (one layer inheritane) Base - Derived
2. Multi-level Inheritance (multi level) Base - Derived - Derived
3. Multiple Inheritance - Derive Class from multiple Base Classes

## `Super` method
It is basically parent class whose properties we are inheriting in the child. Whenever we want to access properties of parent class, we access it with the help of `super()` method

## `@classmethod` 
A class method is bound to the class and receives the class as an implicit first argument

Note - static method can't access or modify class state and generally for utility

## Summery of methods - 
1. class methods
2. instance methods
3. static methods

## `@property`
to handle dynamic behavious of the class attribute (which may dependant on other attributes from same class), We udpate them through the property method 

# Polymorphism : Operator Overloading  

When the same operator is allowed to have different meaning according to the context.  

 - Ek hi cheez ko alg alg tariko se use kiya ja sake toh that comes in the Polymorphism

## Operators & Dunder functions  
double underscore functions in python 

| Operator | Description      | Dunder Function    |
|----------|------------------|--------------------|
| `a + b`  | #addition        | `a.__add__(b)`     |
| `a - b`  | #subtraction     | `a.__sub__(b)`     |
| `a * b`  | #multiplication  | `a.__mul__(b)`     |
| `a / b`  | #division        | `a.__truediv__(b)` |
| `a % b`  | #addition        | `a.__mod__(b)`     |

Apna college Python notes - https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov