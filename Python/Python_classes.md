## Classes in Python

**String representation of instances**:

1. **__str__** --> result when we call **print(object)** .

2. **__repr__** --> Printable representation of the class.
   
   These two are mainly similar and have the purpose of showing the printable representation of the class

**__slots__** :   When the instances are created a lot like more than 1000 instances will be created and this class keeps some data that will not be changed, it is better to keep them in tupple instead of dictionary. Using **slots** wil do this for us and decrease the memory usage. **So use this whenever the instances are created a lot**.

```
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
```

##### **Encapsulating names**:

1. Any name that starts with a single leading **underscore (_) should always be assumed to be internal implementation.**

2. Any name starting with two leading **underscores (__) is called private implementation**. What private implementations give is that mainly they are also internal operations and should be approached carefully. Also, their difference from single underscore is that these implementations are not available in inheritance. Meaning, private methods and properties of the parent **class are not inherited by the child class.**

##### Class Method and Static Method

**Class Method**: These methods are used like alternative constructors.

**Static Method**: To attach to the class, the utility functions somehow related to the class.

**__init__** : is not a constructor
