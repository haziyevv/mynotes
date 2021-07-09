# Collections and Iterables

- **Tuples:**
  
  - If you type one integer inside tuple python will see it as an integer, you should put a comma after it to turn it to tuple

```
In [1]: h = (23)

In [2]: type(h)
Out[2]: int

In [3]: h = (23,)

In [4]: type(h)
Out[4]: tuple
```

- If paranthesis are omitted it still be a tuple
  
  ```
  In [11]: p = 1,2,3,4,5,6
  
  In [12]: type(p)
  Out[12]: tuple
  ```

- **String**:
  
  - Partition method: Divide the string for the seperator and outputs --> **prefix, seperator, suffix**.
  
  ```
  "unforgettable".partition("forget")
  
  ("un", "forget", "able")
  ```

- **List:**
  
  - A list is a mutable object and when we assign list **a** to list **b**, list **b** will take both values and the reference point of list **b**. So changing list **b** will also change list **a** . To cope with this we should copy the list.
  
  - 3 different ways of copying

```
1) list1 = [1,2,3,4]
list2 = list1[:]

2) list1 = [1,2,3,4]
list2 = list1.copy()

3) list1 = [1,2,3,4]
list2 = list(list1)
```

- **Copies as shallow**: When we use .copy() or [:] or list(), it does not matter immutable objects inside the list are copied with their references, so changing them will still change the main list.

- ```
  list1 = [[1,2,3], [2,3,4]]
  list2 = list1.copy()
  
  list2[0][0] = 122
  
  In [1]: list1
  Out[1]: [[122, 2, 3], [2, 3, 4]]
  ```

- to solve this use **copy.deepcopy**() . This will recursively copy the values inside the list.

- ```
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

```
itlist = iter(list_)
next(itlist) --> will give the next element in list
```

3. chain function: concatenates several lists lazily

```
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

```
from collections import namedtuple

Person = namedtuple("Person", "name surname children")

faiq = Person("Faiq", "Haziyev", ["ferid", "tehmez"])
```

# Data Classes

1. How to create a dataclass ? 

```
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str
    children: list
```

# Counter

1. How to create and update a counter to count words in a file ?

```
from collections import Counter

counter = Counter()
with open("filename", "r") as fr:
    for line in fr:
        words = line.split(" ")
        counter.update(words)
```

2. How to select the top 10 most common ?

```

```
