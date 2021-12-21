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

9. **Generic** is used when you want your 

