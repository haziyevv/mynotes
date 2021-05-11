# Functions

1. Parameter ordering:

1- Parameters 2- \*args  3- default params 4- \*\*kwargs

2. What is dictionary unpacking ?

```
def display_name(first, second):
    print(f"My name is {first} {second}")


names = {"first":"Farid", "second":"Haziyev"}
display_name(**names)
```

# OOP

### Properties

```
class Person:
    def __init__(self, age, first, last):
        self._age = age
        self.first = first
        self.second = last
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

### Method Resolution Order (MRO)

1. Shows the hierarcical structure of a class.

```
class Test:
    def __init__(self):
        pass


Test.__mro__
```

### Polymorphism

1. The same class method works in a similar way for different classes

```
class Animal:
    def speak(self):
        raise NotImplementedError("This method should be overriden by subclasses")



class Dog(Animal):
    def speak(self):
        return "bark bark"

class Cat(Animal):
    def speak(self):
        return "meow"
```

### Higher Order Functions

1) When you give a function as a parameter to another function.

2) When there is a nested function inside another function.

### Decorator

1. A function that wraps another function and enhances their behaviour.

```
from functools import wraps
from time import time
import pdb

def speed_test(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time()
        fun(*args, **kwargs)
        end_time = time()
        print(f"Function {fun.__name__} takes {1000 * (end_time - start_time)} unit time")
    return wrapper


@speed_test
def calculate_gen():
    return sum(x for x in range(1000000))


@speed_test
def calculate_list():
    return sum([x for x in range(1000000)])

calculate_gen()
calculate_list()
```

The example below is a decorator for calculating the speeds of any function.







### Caching

1. What is **functools.lru\_cache** and how it is used?  

LRU --> means least recently used. So it keeps the latest n inputs in the cache. We can give a value to **n** as input.

```
@functools.lru_cache(1)
def square(x: float) --> float:
    return x*x
```

Here lru\_cache(1) -> 1 is the number of inputs to remember.



2. 
