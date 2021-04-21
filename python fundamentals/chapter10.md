# Testing





#### Assertion:

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



### Doctests:

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





# Unit Testing

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




