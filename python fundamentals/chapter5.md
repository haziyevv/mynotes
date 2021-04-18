## Collections

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
  
  - A list is a mutable object and when we assign list **a**  to list **b**, list **b** will take both values and the reference point of list **b**. So changing list **b** will also change list **a** . To cope with this we should copy the list.
  
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
