

[TOC]



# Request and Response

**Request Message**

| Request Start line | get/index.html HTTP/1.0                                      |
| ------------------ | ------------------------------------------------------------ |
| **Request Header** | User-Agent: python-requests/2.21.0\n Accept-Encoding: gzip,deflate : |

**Response Message**

| Response Start line | HTTP/1.0 200 OK                                             |
| ------------------- | ----------------------------------------------------------- |
| **Response Header** | Server: Apache-Cache: UNCACHEABLE                           |
| **Response Body**   | <!DOCTYPE html><html><body><h1>My first heading</h1></html> |



**Status Code**

| 1XX  | Informational           |
| ---- | ----------------------- |
| 100  | Everything is so far ok |
| 2xx  | Success                 |
| 200  | Ok                      |
| 3xx  | Redirection             |
| 300  | Multiple Choices        |

| 4XX  | Client Error   |
| ---- | -------------- |
| 401  | Unathorized    |
| 403  | Forbidden      |
| 404  | Not Found      |
| 500  | Server Error   |
| 501  | No Implemented |

* How to send request to http://httpbin.org/get   using name = farid and id=123 with **get request** ?

```
requests.get("https://httpbin.org/get", 
              params={"name":"Farid", "id":123})
```

* How to send **post request** to http://httpbin.org/get using name=farid and id=123 ?

```
requests.post("https://httpbin.org/get",
               params={"name":"Farid", "id":123})
```

## Overview of HTTP

* **Scheme:** http://,  https:://

* **Internet adress or Base URL:** used to find the location, for example: www.ibm.com or www.gitlab.com

* **Route:** location on the web server, example: /images/IDNlogo.png
  
  

# **Logging Library**

1) There are six logging levels in Python. 

2) Highest level is **CRITICAL**. If you set your logging level to **CRITICAL**, only messages of the **CRITICAL** level will be shown.

To set logging level to **CRITICAL**

```
logging.basicConfig(level=logging.CRITICAL)
```

or

```
logging.basicConfig(level=50)
```

3) Logging levels from lowest to highest are: **NOTSET=0**, **DEBUG**=10, **INFO=20**, **WARNING=30**, **ERROR=40**, **CRITICAL=50**.
4. The default level of logging is **WARNING**. Which means, the logging module will only display warnings, errors and critical severity.

5. You can format the logging messages to log in the given format you want. For example you can add the date and time to the log messages:

```
logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', 
                    level= logging.NOTSET)


logging.debug("Here you have some information for debugging.")
logging.info("Everything is normal. Relax!")


--> this will output:

2021-02-14 23:02:34,089 | DEBUG: Here you have some information for debugging.
2021-02-14 23:02:34,089 | INFO: Everything is normal. Relax!

```

Available attributes to use: **[url](https://docs.python.org/3/library/logging.html#logrecord-attributes)**

6. If you want to write the log to a file instead, just add ass atribute to the **logging.basicConfig**

```
logging.basicConfig(filename='sample.log', format='%(asctime)s | %(levelname)s:',
                    level=logging.NotSet)
```



## More advance logging

To use more advanced logging use logger object.

Steps --> 

1) create logger object 

2) set the lowest security level 

3) set a desitination also called a handler. This could be **StreamHandler** to write to console or **FileHandler** to write to a file. 

4) set format of messages for the handler.

```
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler()

log_format = "%(asctime)s | %(levelname)s: %(message)s"
console_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(console_handler)
```



## Loguru

1. to load :

   ```python
   from loguru import logger
   ```

2. File logging with rotation / retention / compression

   ```python
   logger.add("logger_file.log") --> will configure output log file to given file
   logger.add("log_file.log", rotation="5 KB") --> if the size of the file passes 5kb start from clean
   logger.add("out.log", backtrace=True, diagnose=True)  --> will show the full backtrace info
   ```

3. How to use logger in order to catch any exception from a function ?

   ```python
   @logger.catch
   def my_function(x, y, z):
   	return 1/(x+y+z)
   ```

4. If you want async logging:

   ```python
   logger.add("somefile.log", enqueue=True)
   ```



# Python Typing

1. Actually typing does not enforce anything, but it is mostly used for a better and clean code and documentation.

2. But you can use a tool to check and see eveything works fine:

   ```bash
   pip install mypy
   
   mypy main.py
   # this will check typings and find errors
   ```

3. **Dict** type is used for dictionary, **List** type is used for the lists. **Set** type is used for sets.

   ```python 
   from typing import Dict, List, Set
   
   x: List[List[int]] = [[1,2], [3,4,5]]
   x: Dict[str, str] = {'name': 'frodo', 'surname': 'baggins'}
   x: Set[str] = {"frodo", "baggins"}
   ```

4. **Optional** type is used when we say it could be some type or None:

   ```python
   from typing import Optional
   
   def find(num: int, db: List[int]) -> Optional[int]:
   		if num in db:
           return num
       return None
   ```

5. **Sequence** type is used when you want to pass a **list**, **tuple** or a **string**. Anything that can be indexed.

   ```python
   from typing import Sequence
   
   # this will accept both tupple or a list containing strings
   def foo(seq: Sequence[str]):
     	pass
   ```

6. **Tuple** is used for tuples and it is different than other typings. Here you should define the type for all the items inside the tuple

   ```python
   x: Tuple[int, int, int] = [1, 2, 3]
   ```

7. **Callable** is used if you wanted to input a function:

   ```python
   from typing import Callable
   
   def add(x: int, y: int) -> int:
   		return x + y
   
   def foo(func: Callable[[int, int], int]):
   		func(1, 2)
   ```

8. **Union** is used when the value could be of different types. For example int and float

   ```python
   from typing import Union
   
   T = Union[int, float]
   
   def fin_val(val: T, db: List[T]) -> Optional[T]:
     	if val in db:
         	return val
       return None
   ```

9. **Generic** is used when you want your 

9. 



# Python APi development

1. How to create a virtual environment ?

   ```python
   python3 -m venv venv
   
   # a virtual environment named venv will be created
   ```

2. After creating api, fast  api gives you the documentation automatically:

   ```bash
   # if you add /docs to the end of the url it will show the documentation
   # also if you add /redoc it will show a different kind of documentation
   ```

3. What does a serial data type do in postgres ?

   --> used for id, it grows as new row is added.




# Python Basics:

**Python Implementations:**

- Cpython: reference implementation, written in C. This is the standard python implementation

- PyPy: Faster implementation compared to the cpython

- Jython: Python implementation to work with java

- IronPython: Python implementation to work with .net

- PythonNet: Python implementation to work with .net

**BASICS**

* Is a dynamically typed laguage. Object's suitability for a context is determined on runtime.
- Also strongly type language, there is no implicit conversion. Meaning you can not add string and int it will give **TYPE ERROR**

- <u><strong><mark>DO NOT USE MUTABLE OBJECTS SUCH AS LISTS AS DEFAULT ARGUMENTS TO A METHOD</mark></strong></u>

- Is an interpreted language. --> But compiled to bytecode before it is executed

- PEP8 --> python coding standards

- PEP20 --> zen of python. just type **import this**

- ```
  import math
  help(math) --> returns any documentation for math module
  ```

- ```
  float("inf")
  float("nan")    --> converts these to floats
  float("-inf")
  ```

- - [x] Whenever you see nested if statement, fix it using elif.

- random.choices(list, probabilities, k=14) --> will return a list with length 14 from the list input. items with higher probabilities will be returned more often.



# Classes in Python

**String representation of instances**:

1. **__str__** --> result when we call **print(object)** .

2. **__repr__** --> Printable representation of the class.
   
   These two are mainly similar and have the purpose of showing the printable representation of the class

**__slots__** :   When the instances are created a lot like more than 1000 instances will be created and this class keeps some data that will not be changed, it is better to keep them in tupple instead of dictionary. Using **slots** wil do this for us and decrease the memory usage. **So use this whenever the instances are created a lot**.

```
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
```

## Encapsulating names:

1. Any name that starts with a single leading **underscore (_) should always be assumed to be internal implementation.**

2. Any name starting with two leading **underscores (__) is called private implementation**. What private implementations give is that mainly they are also internal operations and should be approached carefully. Also, their difference from single underscore is that these implementations are not available in inheritance. Meaning, private methods and properties of the parent **class are not inherited by the child class.**

## Class Method and Static Method

**Class Method**: These methods are used like alternative constructors.

**Static Method**: To attach to the class, the utility functions somehow related to the class.

**__init__** : is not a constructor



# Collections and Iterables

1. setdefault(key, "Something else") --> returns the value of the given key if it exists else returns the given default.

```python
person = {"name":"Farid", "surname":"Haziyev"}


print(person.setdefault("father_name", "Faiq"))

--> Faiq
```



2. **Tuples:**

- If you type one integer inside tuple python will see it as an integer, you should put a comma after it to turn it to tuple

```python
In [1]: h = (23)

In [2]: type(h)
Out[2]: int

In [3]: h = (23,)

In [4]: type(h)
Out[4]: tuple
```

- If paranthesis are omitted it still be a tuple
  
  ```python
  In [11]: p = 1,2,3,4,5,6
  
  In [12]: type(p)
  Out[12]: tuple
  ```

  

3. **String**:

- Partition method: Divide the string for the seperator and outputs --> **prefix, seperator, suffix**.

```python
"unforgettable".partition("forget")

("un", "forget", "able")
```



4. **List:**

- A list is a mutable object and when we assign list **a** to list **b**, list **b** will take both values and the reference point of list **b**. So changing list **b** will also change list **a** . To cope with this we should copy the list.

- 3 different ways of copying

```python
1) list1 = [1,2,3,4]
list2 = list1[:]

2) list1 = [1,2,3,4]
list2 = list1.copy()

3) list1 = [1,2,3,4]
list2 = list(list1)
```

- **Copies as shallow**: When we use .copy() or [:] or list(), it does not matter immutable objects inside the list are copied with their references, so changing them will still change the main list.

- ```python
  list1 = [[1,2,3], [2,3,4]]
  list2 = list1.copy()
  
  list2[0][0] = 122
  
  In [1]: list1
  Out[1]: [[122, 2, 3], [2, 3, 4]]
  ```

- to solve this use **copy.deepcopy**() . This will recursively copy the values inside the list.

  ```python
  import copy
  list1 = [[1,2,3], [2,3,4]]
  list2 = copy.deepcopy(list1)
  In [19]: list2[0][0] = "aa"
  
  In [20]: list1
  Out[20]: [[1, 2, 3], [2, 3, 4]]
  ```




## Iterables

1. Iterable : something that can be iterated (set, list, dictionary, tuple)

2. iterator: Using iter() function iterable is changed to iterator, on which we can iteratre over.

```python
itlist = iter(list_)
next(itlist) --> will give the next element in list
```

3. chain function: concatenates several lists lazily

```python
from itertools import chain

a1  = [1,2,3,4,5]
a2  = [2,2,2,2,2]

a3 = chain(a1, a2)
In [34]: a3
Out[34]: <itertools.chain at 0x7ff1bd65a760>
In [35]: list(a3)
Out[35]: [1, 2, 3, 4, 5, 2, 2, 2, 2, 2]
```



## NamedTuples

1. How to create a named tuple ? 

```python
from collections import namedtuple

Person = namedtuple("Person", "name surname children")

faiq = Person("Faiq", "Haziyev", ["ferid", "tehmez"])

CandidateInfoTuple = namedtuple(
    'CandidateInfoTuple',
    'isNodule_bool, diameter_mm, series_uid, center_xyz',
)


--> first string is the name
--> others are keys


candidateInfo_list.append(CandidateInfoTuple(
                isNodule_bool,
                candidateDiameter_mm,
                series_uid,
                candidateCenter_xyz,
```



## Data Classes

1. How to create a dataclass ? 

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str
    children: list
```



## Counter

1. How to create and update a counter to count words in a file ?

```python
from collections import Counter

counter = Counter()
with open("filename", "r") as fr:
    for line in fr:
        words = line.split(" ")
        counter.update(words)
```

2. How to select the top 10 most common ?



# Python Command Line

1. Depending on the compexity of your **CLI** you usually have parameters to pass to the scripts which can either be:
   - **Argument** - mandatory parameter that's passed to the script
   - **Option** - optional parameter combining a name and a value
   - **flag** - to enable or disable a certain behaviour



# Python Concurrency

1. What does Thread-safe mean ?
2. Research about deadlock ?
3. task\_que.get(block=False) ?
4. In cpython no 2 threads can run at the same time 
5. sys.getrefcount(a) --> shows number of references to the object "a"

**Reference count** --> obyekte olan müraciet sayıdır. Eger bu sıfır olarsa **garbage collector** bu obyekti silir yaddaşdan.

IO bound vs cpu bound -- > with io bound you can use multithreading. But with cpu bound functions multithreading is not working. 





6.  Most high level and easy to use parallel processing features are given by **concurrent.futures**

```
from concurrent.futures import , ProcessPoolExecutor


with ThreadPoolExecutor() as exec:
    exec.map(func, arguments_list)
```

example:

```
def error_calc(audio_file):
    key_ = audio_file.split("/")[-1].split(".")[0]
    error_ = get_error_rate(audio_file, texts[key_])
    return error_

with ThreadPoolExecutor() as exec:
    exec.map(func, audio_files)
```




## Asyncio

1. Asyncio is created to fix the context switching problem in threading. In threading each time one thread os stopped and context is switched to the other thread to do its task. 

1. Asynchronous means for example: you have 10 urls that you have to send request. You send one request and then cpu does not sleep and wait for the response, it goes to the second url and like this.

1. A **coroutine** is a function that can suspend its execution before reaching return and it can directly pass control to some other **coroutine** for some time.

1. What is an **event loop** ?

   - There is a queue of events and a loop that constantly pulls events off the queue and runs them. These events are called **coroutines**.

1. How to create an event loop and run a coroutine ?

   ```python
   import asyncio
   
   async def main():
   	print('salam qaqa')
   asyncio.run(main())
   ```

6. Runs in a single process and a single thread. 

7. Everything is happening within 1 thread and 1 process.

8. **Await** --> where it is safe for asyncio to go another coroutine. Generally it is where we are waiting for some io to complete.

9. **Coroutine** --> This is just a stateful subroutine, namely function. Its difference and advantage from  a function is that when you invoke a function again it does not remember anything and starts from beginning, but with coroutines it continues from where it left. 

7. When you use **await f()** -- **f** function should be awaitable. This means it is another coroutine, or an object defining an **\_\_await\_\_** dunder method.



# Exception Handling

**Index Error**: When the integer index is not in the range

**Key Error**: When the key does not exist in the lookup

**Value Error:** Object is of the right type, but contains inapropriate value for the operation. In the example below we can see that. Input type is correct, it is a string but a string that can not be converted to integer.

```
def converter(s: str) -> int:
    x = int(s)
    return x



In [2]: converter("alma")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-684f7a9b4202> in <module>
----> 1 converter("alma")

<ipython-input-1-f8f112efece0> in converter(s)
      1 def converter(s: str) -> int:
----> 2     x = int(s)
      3     return x

ValueError: invalid literal for int() with base 10: 'alma'
```

**Type Error**: Object is not of the right type. In the example below, string or byte or int is expected, but input was a list.

```
In [3]: converter([1,2,3,4])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-c417cd5701e1> in <module>
----> 1 converter([1,2,3,4])

<ipython-input-1-f8f112efece0> in converter(s)
      1 def converter(s: str) -> int:
----> 2     x = int(s)
      3     return x

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
```

- [x] Avoid doing this:

```
try:
    do_something
except:
pass
```

or

```
try:
    do_something
except Exception as e
    print(e)
```

If you pass, or catch any exception, the you will not know what causes the error.



# Python Files - I/O

1. Explain **os.walk**:
- It lets you run through every directory and file inside a given path:

```
import os

for root, dirnames, filenames in os.walk("mynotes"):
    
```

--> Here at first, **root** will be the **mynotes** and **dirnames** will be all the directories inside **mynotes** folder, and **filenames** will be all the files inside **mynotes** folder directly, not inside any folder in the **mynotes**. 

--> In next iteration it will enter the first **dirname** inside the **root**. This time **root** will be that dirname.

2. Explain **pathlib**:
* Object Oriented, makes it more clean than os.path

```python
from pathlib import Path

path = Path("Documents") / "mynotes"
```

* It has **glob** and **rglob** methods available. **glob** will return files matching the pattern in the given directory, but **rglob** will return files that match the pattern in any directory inside the given directory.

```python
[x for x in path.rglob("*.md")]  --> will return all the files with 
--> .md extension inside the path and in all of its subdirectories
```

3. Parse xml:
   * One possible solution is **ElementTree**

```python
import xml.etree.ElementTree as ET

tree = ET.parse("some_data.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
```





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

## Properties

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

## Method Resolution Order (MRO)

1. Shows the hierarcical structure of a class.

```
class Test:
    def __init__(self):
        pass


Test.__mro__
```

## Polymorphism

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

## Higher Order Functions

1) When you give a function as a parameter to another function.

2) When there is a nested function inside another function.

## Decorator

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



# Caching

1. What is **functools.lru\_cache** and how it is used?  

LRU --> means least recently used. So it keeps the latest n inputs in the cache. We can give a value to **n** as input.

```
@functools.lru_cache(1)
def square(x: float) --> float:
    return x*x
```

Here lru\_cache(1) -> 1 is the number of inputs to remember.



## Functools

1. How to convert sequential operations like in machine learning models, to composite function ?

   ex:

   ```python
   # before
   class Model:
       
       def __init__(self):
           self.linear1 = nn.Linear()
           self.relu1 = nn.ReLU()
           self.linear2 = nn.Linear()
           self.relu2 = nn.ReLU()
      	
       def forward(self, x):
           x = self.linear1(x)
           x = self.relu1(x)
           x = self.linear2(x)
           x = self.relu2(x)
           return x
   
   # after
   class Model:
       
       def __init__(self):
           self.linear1 = nn.Linear()
           self.relu1 = nn.ReLU()
           self.linear2 = nn.Linear()
           self.relu2 = nn.ReLU()
       
       def compose(self, *functions):
           return functools.reduce(lambda f,g: lambda x: g(f(x)) ,functions)
       
       def forward(self, x):
           myfunc = compose(self.linear1, self.relu1, self.linear2, self.relu2)
           return myfunc(x)
   
   ```



# Modules, Scripts and Programs

**Module**: Any .py code is a module. Mainly modules are convenient to import with api.

**Script**: any simple python code, that is more compatible to run from terminal rather than using it in an api.

**Program**: Composed of many modules.

##### Modules:

- ```
  from word import (fetch_words, print_words) --> we can import several 
                              functions from the word module like this
  ```

- **CODE OF ZEN**: Sparse is better than Dense. You should put two blank lines between the functions.

- **Docstring**: (documentation of the module)
  
  - In the first line use it as an information about what the module do in general, and how to run it
  
  - ```
    """
    What this module does in general, what is its purpose?
    Usage: python3 module_frodo.py "frodo baggıns"
    """
    ```
  
  - In each function add docstring, explaining the purpose of the function, what it does, input arguments and what it will return
  
  - ```
    """
    This function will make the life a better place for us.
    Args:
        url: the url you want to connect
        age: your age
    Returns:
        A list of movies that u could watch
    """
    ```



# Python Questions

1. What is the line limit for PEP-8 in python ?

2. What is an identifier ?

3. How to check if all characters in a string are alphanumeric ?

4. How do you find, which directory you are currently in?

5. Explain these builtin functions :
   
   * eval()
   
   * filter()
   
   * map()
   
   * hash()
   
   * hex()

6. Is **del** the same as **remove** ?

7. How to make a python directory executable ?

8. What is closure ?
   
   Local function remembers the variables created in the local enclosing function. 

9. What does first class functions mean ?

10. What is a function factory ? 
    
    Function that returns new, specialised function.

11. How does python subprocess work ?

Its main purpose is to write shell commands on python.

```
import subprocess
subprocess.run(["cp", source, target]) --> this is similar to 
"cp source target"
```

12. How does **strftime** work in python ?
    * Returns datetime object as a string in a given format.

```
template = "%Y-%h-%d %H:%M:%S"
now = datetime.now()
nowstr = now.strftime(template)
```





# Strings and Collections

**String: str** --> immutable sequences of unicode codepoints.

**Multiline Strings**: String below will be written as multiline. Each row is a line.

```
"""
Mene deniz verin,
O tenha qalıb,
O meni axtarır,
Meni gözleyir
"""
```

**Raw strings:** r before the string.

```
path = 'C:\Users\frodo\documents\bagginss' --> this will give errors
path = r'C:\Users\frodo\documents\bagginss' --> this will run clean
```



# Testing

## Assertion:

1) can be used for testing like this:
   
   ```
   def eat_junk(food):
       assert food in {"burger", "pizza", "candy"}
       return "tasty food"
   
   
   python3 -c "from testing import eat_junk; eat_junk('burger')"
   --> tasty food
   
   
   python3 -c "from testing import eat_junk; eat_junk('apple')"
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
     File "/home/haziyevv/testing.py", line 3, in eat_junk
       assert food in {"burger", "pizza", "candy"}, "This is not a junk food"
   AssertionError: This is not a junk food
   ```
2. Can be ignored when -**O (optimisation)** flag is used
   
   ```
   python3 -O  -c "from testing import eat_junk; eat_junk('apple')"
   tasty food
   ```



## Doctests:

1. Can be used inside of the docstring easily to test the function. But is very messy. 

An example:

```
def add_nums(num1, num2):
    """Should return sum of the inserted positive numbers.
        >>> add_nums(2, 22)
        24
        >>> add_nums(3, -1)
        'Enter a positive number'
    """
    pass
```



Module should be called like this:

```
python3 -m doctest -v testing.py
```

returns:

```
Trying:
    add_nums(2, 22)
Expecting:
    24
**********************************************************************
File "/home/haziyevv/testing.py", line 5, in testing.add_nums
Failed example:
    add_nums(2, 22)
Expected:
    24
Got nothing
Trying:
    add_nums(3, -1)
Expecting:
    'Enter a positive number'
**********************************************************************
File "/home/haziyevv/testing.py", line 7, in testing.add_nums
Failed example:
    add_nums(3, -1)
Expected:
    'Enter a positive number'
Got nothing
1 items had no tests:
    testing
**********************************************************************
1 items had failures:
   2 of   2 in testing.add_nums
2 tests in 2 items.
0 passed and 2 failed.
***Test Failed*** 2 failures.
```



## Unit Testing

1. Encapsulated as classes that inherit from **unittest.TestCase**

```
class SomeTests(unittest.TestCase):
```

2. Run tests by calling:

```
unittest.main()
```

3. Example:

```
import unittest

def eat(food: str) -> bool:
    return True if food == "apple" else False


class FoodTest(unittest.TestCase):
    def test_healty_food(self):
        self.assertEqual(eat("apple"), True)

if __name__=="__main__":
    unittest.main()
```



4. There we can also use **assertTrue**:

```
self.assertTrue(eat("apple"))
```

5. You can also add your exception message:
   
   ```
   self.assertEqual(eat("apple"), True, "Eat healthy die healthy")
   ```

6. **Before and after hooks**. You may need to acces to an instance or you may need to add something to database. Instead of creating an instance each time, you can create and destory it in each instance with **setUp** and **tearDown** methods.

```
class ActivitiesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("farid", 29)

    def test_name(self):
        self.assertEqual(self.person.get_person_name(), "farid")

    def test_age(self):
        self.assertEqual(self.person.get_person_age(), 29)
```





# Pipenv and Virtual Environments

## **Pipenv**:

Dependency manager for python projects.

Manages dependencies on a per-project basis.

```
 pipenv install requests
```

--> this command will install requests library and create a Pipfile file where all the dependencies will be added.

```
pipenv run python main.py 
```

--> this way we run the main script. We add pipenv before, to ensure installed pipenv packages are available to the python script. İf we do not add pipenv before, libraries installed by pipenv for this project will not be accessible to the python script.

## **Virtualenv**

```
pip install virtualenv
virtualenv testing
```

--> installs virtualenv and creates a virtualenv named testing in the given directory.

```
to activate: source testing/bin/activate
```

## VirtualEnvWrapper

```
pip install virtualenvwrapper
export WORKON_HOME=~/ENVS
source ./local/bin/virtualenvwrapper.sh
```

first command installs virtualenvwrapper.

second command exports its main directory where all the created virtual environments will be installed.

third command activates the virtual environment wrapper

```
mkvirtualenv venv --> creates a virtual environment named venv in ENVS folder
workon venv --> activates the venv virtual environment
```



## VENV

```bash
sudo apt install python3.8-venv

# create virtual environment named venv
python3 -m venv venv 
```



# Python Deployment

1. What is **wheel** and when to use it ?

   --> Python wheel is used to create a built distribution to share with your users.



# Kubernetes Task

**Task:** Build a Docker container image from provided code and a Dockerfile using Cloud Build. Then upload the container to Container Registry.

**Objectives**: Use Cloud Build to build and push containers. Use Container Registry to store and deploy containers.



1. create a Dockerfile:

   ```bash
   FROM alpine
   COPY quickstart.sh /
   CMD ["/quickstart.sh"]
   ```

2. - In Cloud Shell, run the following command to build the Docker container image in Cloud Build.

     ```bash
     gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/quickstart-image .
     ```

   - Other possible way is:

     create a yaml file cloudbuild.yaml:

     ```bash
     steps:
     - name: 'gcr.io/cloud-builders/docker'
       args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
     images:
     - 'gcr.io/$PROJECT_ID/quickstart-image'
     ```

     then:

     ```bash
     gcloud builds submit --config cloudbuild.yaml .
     ```

   - Another possible yaml that tests the container:

     ```bash
     steps:
     - name: 'gcr.io/cloud-builders/docker'
       args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
     - name: 'gcr.io/$PROJECT_ID/quickstart-image'
       args: ['fail']
     images:
     - 'gcr.io/$PROJECT_ID/quickstart-image
     ```


# Tips

1. What is DRY principle in python ? 

   --> It is, do not repeat yourself. If you see that you are copying and pasting, then you should consider writing a function.





# Pyton OOP

1. **Composition** is the act to collect several objects together, and create a new one.
   - It is a good choice, when one object is part of another object.

2. Python classes should be named like this: **CamelCase**

3. ```bash
   python -i first_class.py
   
   # will run the code and then go to interactive mode
   ```

4. \_\_new\_\_ is used for constructor

5. Properties starting with __ double underscore can not be riched publicly. You should use a trick like:

   ```python
   class SecretString:
   	def init(self, plain_text):
   		self.__plain_text = plain_text
   
   secret = SecretString('hi there')
   secret.__plain_text --> will not work
   secret._SecretString__plain_text --> should be called for that variable
   ```

6. To install pip:

   ```bash
   sudo python -m ensurepip
   ```

7. The simples and most useful form of multiple inheritance is called a **mixin**

8. A **mixin** is generally a superclass that is not meant to exist on its own, but is meant to be inherited by some other class to provide some extra functionality.

9. 

