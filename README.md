# Overloading Operators in Python

- [Overloading Operators in Python](#overloading-operators-in-python)
  - [Introduction](#introduction)
  - [Python Basics and Preliminaries](#python-basics-and-preliminaries)
  - [Overloading Arithmetic Operators](#overloading-arithmetic-operators)
  - [Overlaoading Comparison Operators](#overlaoading-comparison-operators)
  - [Conclusion](#conclusion)

## Introduction

Hello, our names are Armand Sarkezians and Dane Gledhill. We are students at the University of Toronto, Scarborough Campus. As a part of our CSCC24 Exercise 6, we will take you through this markdown document and show you (the reader) how to overload operators in Python. We are also learning this topic, so every small fact and tidbit we come across will be shared, and code will be provided. Join us, as we jump into the preliminaries when it comes to coding in Python.

## Python Basics and Preliminaries

Python allows coders to develop their own types. This can be done by using the `class` keyword. An example is shown below:

```python
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Volkswagen", "Jetta", "2015")
car2 = Car("Ford", "Fiesta", "2016")
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

Before we talk about operator overloading, we must first talk about why I denoted the function `__init__` using underscores. This is called a 'special function' in python.These functions can get called in a variety of ways. For example, when we create a new instance of the class, the `__init__` function is called. We can also call the `__init__` function from within the class itself.

These functions are vital for operator overloading. They are used to define how the operators `+`, `-`, `*`, and `/` work with the objects of the class. In the following sections, we will discuss how these operators can be overloaded in python.

## Overloading Arithmetic Operators

## Overlaoading Comparison Operators

## Conclusion
