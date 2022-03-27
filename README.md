# Overloading Operators in Python

- [Overloading Operators in Python](#overloading-operators-in-python)
  - [Introduction](#introduction)
  - [Python Basics](#python-basics)
    - [Connection to Course Materials](#connection-to-course-materials)
    - [Preliminaries](#preliminaries)
  - [Overloading Arithmetic Operators](#overloading-arithmetic-operators)
    - [Addition and Subtraction](#addition-and-subtraction)
    - [The rest](#the-rest)
    - [Connection to Class Materials](#connection-to-class-materials)
  - [Overlaoading Comparison Operators](#overlaoading-comparison-operators)
  - [Conclusion](#conclusion)

## Introduction

Hello, our names are Armand Sarkezians and Dane Gledhill. We are students at the University of Toronto, Scarborough Campus. As a part of our CSCC24 Exercise 6, we will take you through this markdown document and show you (the reader) how to overload operators in Python. We are also learning this topic, so every small fact and tidbit we come across will be shared, and code will be provided. Join us, as we jump into the preliminaries when it comes to coding in Python.

## Python Basics

Python allows coders to develop their own types. These types are called classes. Classes are a way to group together related variables and functions. These are implemented by using the `class` keyword. An example is shown below:

```python
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Volkswagen", "Jetta", 2015)
car2 = Car("Ford", "Fiesta", 2016)
print(car1 + car2)
```

In this example, we define a `Car` class. The `__init__` method is called when a new instance of the class is created. The `__init__` method takes three parameters, `make`, `model`, and `year`. The `make` and `model` parameters are assigned to the `self.make` and `self.model` attributes, respectively. The `year` parameter is assigned to the `self.year` attribute. When we try to add these two objects together, the following error will print:

```bash
Traceback (most recent call last):
  File "/path/Car.py", line 10, in <module>
    print(car1 + car2)
TypeError: unsupported operand type(s) for +: 'Car' and 'Car'
```

This error states that two objects of type `Car` cannot be added together. This is because the python interpreter does not know how to add two objects of type `Car`. We must define these ourselves.

### Connection to Course Materials

In order to clear up any confusion that these classes may bring to someone who is new to Python, we will make a clear connection to our course materials.Specifically, we will compare Python types to those found in Haskell. In Python, every new type defined is a class, in Haskell, types can be defined as data types. An example of the same Car class in Haskell is shown below, using a data type:

```haskell
data Car = Car { make :: String, model :: String, year :: Int }
```

Both of these data types include the same parameters, the stirng `make`,  the string `model`, and the integer `year`. The difference between these types, aside from syntax, comes from their instantiation. For the class, instantiation of a type can be altered, using the `__init__` method. For the data type, instantiation can not altered.

Essentially, in Python and Haskell, types are created to more  easily identify grouped together components. A single car object is more easy to work with then three seperate data types (String, String, Int).

### Preliminaries

Before we talk about operator overloading in Python, we must first talk about why I denoted the function `__init__` using underscores. This is called a 'special function' in python.These functions can get called in a variety of ways. For example, when we create a new instance of the class, the `__init__` function is called. We can also call the `__init__` function from within the class itself.

These functions are vital for operator overloading. They are used to define how the operators `+`, `-`, `*`, and `/` work with the objects of the class. In the following sections, we will discuss how these operators can be overloaded in python.

## Overloading Arithmetic Operators

In Python, overloading arithmetic operators is a very simple process. We simply define a function with the same name as the operator, and then define the function to perform the operation. The specifics for each operation are shown below.

### Addition and Subtraction

In order to overload the `+` and `-` operators, we must define a function with the same name as the operator. The function must take two parameters, `self` and `other`. The `self` parameter is the object that is being added to, and the `other` parameter is the object that is being added. The function must return the result of the operation. An extended Car Class is shown below:

```python
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __add__ (self, other):
        return Car(self.make, self.model, self.year + other.year)

car1 = Car("Volkswagen", "Jetta", 2015)
car2 = Car("Ford", "Fiesta", 2016)
print(car1 + car2)
```

The following snippet outputs:

```bash
4031
```

Instead of returning an error, the addition of the `__add__` function will return a new instance of the class. When two instances of a class are added, Python looks for a `__add__` function. If one is found, it is called. If no `__add__` function is found, Python will return an error. Creating this function in the class you defined then allows you to overload the `+` operator, to whatever you want (it does not need to be addition, you can overload the `__add__` function to create a whole tetris minigame if you wanted to).

A similar concept is used for the `-` operator. The `__sub__` special function is defined, and used to overload the `-` operator. The `__sub__` function takes two parameters, `self` and `other`. The `self` parameter is the object that is being subtracted from, and the `other` parameter is the object that is being subtracted. The function must return the result of the operation. An example of this is shown below.

```python
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __sub__ (self, other):
        return self.year - other.year

car1 = Car("Volkswagen", "Jetta", 2015)
car2 = Car("Ford", "Fiesta", 2016)
print(car1 - car2)
```

The following snippet outputs:

```bash
-1
```

Overloading arithmetic operators in Python is easy, and I'm sure none of you will have any trouble with it. =)

### The rest

Now that we have looked into addition and subtraction in detail, instead of repeating the same time 50 times, I will list the special functions needed for overloading arithmetic operators in Python. Some of the functions may require a little clarification, which I will try to provide. In any case, if you are confused to need extra information, please look to the [Python Official Documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names) for more information.

Additional special functions:

- Multiplication = `__mul__`
  - `__mul__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being multiplied, and the `other` parameter is the object that is being multiplied. The function must return the result of the operation.  

- Division = `__truediv__`
  - `__truediv__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being divided, and the `other` parameter is the object that is being divided. The function must return the result of the operation.

- Power = `__pow__`
  - `__pow__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being raised to a power, and the `other` parameter is the object that is being raised to a power. The function must return the result of the operation.

- Floor Division = `__floordiv__`
  - `__floordiv__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being divided, and the `other` parameter is the object that is being divided. The function must return the result of the operation.

- Remainder = `__mod__`
  - `__mod__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being divided, and the `other` parameter is the object that is being divided. The function must return the result of the operation.

- Bitwise left shift = `__lshift__`
  - `__lshift__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being left shifted, and the `other` parameter is the object that is being left shifted. The function must return the result of the operation.

- Bitwise right shift = `__rshift__`
  - `__rshift__` takes two parameters, `self` and `other`. The `self` parameter is the object that is being right shifted, and the `other` parameter is the object that is being right shifted. The function must return the result of the operation.

### Connection to Class Materials

## Overlaoading Comparison Operators

## Conclusion
