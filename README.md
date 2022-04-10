# Overloading Operators in Python

- [Overloading Operators in Python](#overloading-operators-in-python)
  - [Introduction](#introduction)
  - [Python Basics](#python-basics)
    - [Connection to Course Materials](#connection-to-course-materials)
    - [Preliminaries](#preliminaries)
  - [Overloading Arithmetic Operators](#overloading-arithmetic-operators)
    - [Addition and Subtraction](#addition-and-subtraction)
    - [Other Functions](#other-functions)
    - [Connection to Class Materials](#connection-to-class-materials)
  - [Overloading Comparison Operators](#overloading-comparison-operators)
    - [Equals and String Representation](#equals-and-string-representation)
    - [Comparison to Class Materials](#comparison-to-class-materials)
    - [Additional Comparison Operators](#additional-comparison-operators)
  - [Conclusion](#conclusion)
    - [References](#references)

## Introduction

Hello, our names are Armand Sarkezians and Dane Gledhill. We are students at the University of Toronto, Scarborough Campus. As a part of our CSCC24 Exercise 6, we will take you through this Markdown document and show you (the reader) how to overload operators in Python. We are also learning this topic, so every small fact and tidbit we come across will be shared, and code will be provided. Join us, as we jump into the preliminaries when it comes to coding in Python.

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

In order to clear up any confusion that these classes may bring to someone who is new to Python, we will make a clear connection to our course materials. Specifically, we will compare Python types to those found in Haskell. In Python, every new type defined is a class, in Haskell, types can be defined as new types. An example of the same Car class in Haskell is shown below, using a new type:

```haskell
newtype Car make model year = Car (make, model, year) deriving (Eq, Show)
```

Both of these data types include the same parameters, the string `make`, the string `model`, and the integer `year`. The difference between these types, aside from syntax, comes from their instantiation. For the class, instantiation of a type can be altered, using the `__init__` method. For the new type, instantiation can not be altered.

Essentially, in Python and Haskell, types are created to more easily identify grouped together components. A single car object is easier to work with than three separate data types (String, String, Int).

### Preliminaries

Before we talk about operator overloading in Python, we must first talk about why I denoted the function `__init__` using underscores. This is called a 'special function' in python. These functions can get called in a variety of ways. For example, when we create a new instance of the class, the `__init__` function is called. We can also call the `__init__` function from within the class itself.

These functions are vital for operator overloading. They are used in defining how the operators `+`, `-`, `*`, and `/` work with the objects of the class. In the following sections, we will discuss how these operators can be overloaded in python.

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
      return self.year + other.year

car1 = Car("Volkswagen", "Jetta", 2015)
car2 = Car("Ford", "Fiesta", 2016)
print(car1 + car2)
```

The following snippet outputs:

```bash
4031
```

Instead of returning an error, the addition of the `__add__` function will return an integer. When two instances of a class are added, Python looks for a `__add__` function. If one is found, it is called. If no `__add__` function is found, Python will return an error. Creating this function in the class you defined then allows you to overload the `+` operator, to whatever you want (it does not need to be addition, you can overload the `__add__` function to create a whole Tetris mini-game if you wanted to).

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

### Other Functions

Now that we have looked into addition and subtraction in detail, instead of repeating the same thing 50 times, I will list the special functions needed for overloading arithmetic operators in Python. Some functions may require a little clarification, which I will try to provide in a small blurb at the bottom of the list. In any case, if you are confused or need extra information, please look to the [Python Official Documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names) for more information.

Additional special functions:

- Multiplication = `__mul__`
- Division = `__truediv__`
- Power = `__pow__`
- Floor Division = `__floordiv__`
- Remainder = `__mod__`
- Bitwise left shift = `__lshift__`
- Bitwise right shift = `__rshift__`

All of these special functions require takes two parameters, `self` and `other`. They apply their respective operations on these two objects. All of these functions are binary operators, and work left associatively for non-binary operations.

### Connection to Class Materials

Special functions are not an entirely new concept. We have seen them before in class, albeit with comparison operators instead of arithmetic operators. I will show you all how to overload arithmetic operators in Haskell. The syntax is not unlike the 'Eq' and 'Show' instances we have seen in class. The example below is using the same definition of `Car` we have defined above.

```haskell
newtype Car make model year = Car (make, model, year) deriving (Eq, Show)

instance (Num make, Num model, Num year) => Num (Car make model year) where
  Car (make1, model1, year1) + Car (make2, model2, year2) = Car (make1, model1, year1 + year2)
  Car (make1, model1, year1) - Car (make2, model2, year2) = Car (make1, model1, year1 - year2)
  Car (make1, model1, year1) * Car (make2, model2, year2) = Car (make1, model1, year1 * year2)
  Car (make1, model1, year1) / Car (make2, model2, year2) = Car (make1, model1, year1 / year2)
  abs (Car (make, model, year)) = Car (make, model, abs year)
```

The following code bit overloads addition, multiplication, division, subtraction, and absolutes in Haskell. After describing how to overload comparison operators in Python, I will show the connection between this bit of code, and that of which we have seen in class (overloading Eq and Show).

## Overloading Comparison Operators

In Python, the overloading of arithmetic and comparison operators are very similar. We must define a function with the same name as the operator, and then define the function to perform the operation. The specifics for each operation are shown below.

### Equals and String Representation

Like addition and subtraction, special functions must be used here. In order to overload the '==' operator, we must defined the `__eq__` special function. The `__eq__` function takes two parameters, `self` and `other`. The `self` parameter is the object that is being compared to, and the `other` parameter is the object that is being compared. The function must return a boolean value. An example of this is shown below.

```python
class Car:
    def __init__ (self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

    def __eq__ (self, other):
      return self.year == other.year
```

This code blurb defines equality between two cars. If two cars are made on the same year, I can say that they are equal. Again, this equality does not need to be logically true. You can define this class to do whatever you want it to do. If your heart desired, you could write a `__eq__` function that always returns true.

There is a similar way to overload the string representation of an object. If we were to create two cars without the overloaded string representation, Python would output the address of the object, as such:

```python
class Car:
    def __init__ (self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

car1 = Car("Ford", "Fiesta", 2016)
print(car1)
```

Output:

```python
<__main__.Car object at 0x7f8b8b8b8d10>
```

We need to create the function `__str__` in order to overload the string representation of our Car object. The `__str__` function takes one parameter, `self`. The `self` parameter is the object that is being represented. The function must return a string. An example of this is shown below.

```python
class Car:
    def __init__ (self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

    def __str__ (self):
      return "{} {} {}".format(self.make, self.model, self.year)

car1 = Car("Ford", "Fiesta", 2016)
print(car1)
```

Output:

```python
Ford Fiesta 2016
```

### Comparison to Class Materials

These operators are not unlike the ones we have seen in class. Both overloading in Haskell and Python require you to develop functions with specific names, and define your return values based on the objects parameters. A definition for overloading Haskell `Eq` and `Show` are shown below.

```haskell
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)

class Show a where
    show :: a -> String
```

Some key ideas to note:

- In both Python and Haskell, you do not need to overload the 'not equals' operators. You, however, can if you want to. Both of these functions can either have their own logic, or be defined in terms of the 'equals' operator. It is up to you.
- Haskell needs a class or instance of Eq in order to overload the 'equals' operator, however, Python needs the function to be defined in a specific class. This means that in Haskell, you could have all of your equals operators defined in one file, but in Python, you would need to define them in a separate file, specifically in the class that you want them to be defined in.

### Additional Comparison Operators

Some addition comparison operators are shown below. These have near identical syntax to the `__eq__` and `__str__` functions, therefore, I will not be going in depth into them. Feel free to read through the official [Python documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names) for these operators.

- Less than = `__lt__`
- Less than or equal to = `__le__`
- Not Equal to = `__ne__`
- Greater than = `__gt__`
- Greater than or equal to = `__ge__`
- String representation = `__repr__`
  - Keep in mind that `__str__` is not the same as `__repr__`. The `__repr__` function is the "official" string representation of an object, whereas `__str__` is informal. Both should be defined in the same class, however, if only `__repr__` is defined, it will be used.
- Hash value = `__hash__`

## Conclusion

We are now done. Congratulations! You have completed our course on Python Operator Overloading! We hope you enjoyed this document, we have enjoyed writing it. If you have any questions, learn how to google or read documentation. Thanks for reading!

### References

We only used the official Python documentation for this lesson. Find the full documentation [here](https://docs.python.org/3/reference/datamodel.html#special-method-names).
