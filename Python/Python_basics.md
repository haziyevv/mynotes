## Python implementations:

Cpython: reference implementation, written in C. This is the standard python implementation

PyPy: Faster implementation compared to the cpython

Jython: Python implementation to work with java

IronPython: Python implementation to work with .net

PythonNet: Python implementation to work with .net



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
