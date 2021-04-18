## Iterables

1) Iterable : something that can be iterated (set, list, dictionary, tuple)

2) iterator: Using iter() function iterable is changed to iterator, on which we can iteratre over.

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

