# Testing

> [!IMPORTANT]
>
> **! Unit tests should not depend on resources like internet connections, network, endpoints etc**

> [!IMPORTANT]
>
> **If you intend to test real API calls you should create integration test project and use it for this purpose. But be aware integration tests are mostly not repeatable and would give you different results on each run.**

## Unit Testing

1. Encapsulated as classes that inherit from **unittest.TestCase**

```python
class SomeTests(unittest.TestCase):
```

2. Run tests by calling:

```python
unittest.main()
```

3. Example:

```python
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

```python
self.assertTrue(eat("apple"))
```

5. You can also add your exception message:

   ```python
   self.assertEqual(eat("apple"), True, "Eat healthy die healthy")
   ```

6. **Before and after hooks**. You may need to acces to an instance or you may need to add something to database. Instead of creating an instance each time, you can create and destory it in each instance with **setUp** and **tearDown** methods.

```python
class ActivitiesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("farid", 29)

    def test_name(self):
        self.assertEqual(self.person.get_person_name(), "farid")

    def test_age(self):
        self.assertEqual(self.person.get_person_age(), 29)
```



# Pytest

1. ```python
     from unittest.mock import patch, Mock
     
     with patch('builtins.open'), \
         patch('pickle.load') as mock_load, \
         patch('entity_resolution.app.base_vectorizer', base_vectorizer):
         mock_load.return_value = base_vectorizer
         yield base_vectorizer
   ```

   This code snippet is part of a pytest fixture (mock_vectorizers) and demonstrates mocking/patching behavior in Python testing. Let me break down what it does:

   ```python
   with patch('builtins.open')
   
   # This mocks Python's built-in open() function
   # Prevents actual file operations during testing
   ```

   ```python
   patch('pickle.load') as mock_load
   
   # Mocks Python's pickle.load function
   # Captures the mock in the mock_load variable
   ```

   ```python
   mock_load.return_value = base_vectorizer 
   # sets up the mock to return the base_vectorizer whenever pickle.load is called
   ```

   ```python
   patch('entity_resolution.app.base_vectorizer', base_vectorizer)
   
   # Replaces the actual base_vectorizer in the application with the test mock version
   ```

   

   This is a pytest fixture pattern that provides the mock vectorizer to any test that uses this fixture

   After the test completes, the context manager (with statement) ensures all mocks are cleaned up

   

   **The overall purpose is to:**

   - Prevent actual file I/O during testing
   - Provide a controlled, predictable test environment
   - Replace the real vectorizer with a test double that has known behavior
   - Allow tests to run without loading actual model files or data
   - This is particularly useful for integration tests where you want to test the API endpoints without depending on actual model files or real data.

2. Check if something is expected to be `True` or `False`

   ```python
   import pytest
   
   def squared(number):
     return number*number
   
   def test_squared():
     assert squared(-2) == squared(2)
   
   def test_false():
     assert squared(3) != squared(3)
   ```

3. Test when you expect to raise an error:

   ```python
   import pytest
   
   def division(a, b):
     return a / b
   
   def test_raises():
     with pytest.raise(ZeroDivisionError):
       division(a=25, b=0)
   ```

4. In order to run only selected tests with filtering

   ```python
   # will only run the tests functions with word multiplication inside
   pytest tests -k 'multiplication' 
   ```

5. Pytest markers:

   - In **pytest**, markers are special labels that you can assign to test functions or classes to organize, categorize, or control their execution. Types:

     - Skip: just ignore the testing. Could be the method is not yet implemented
     - Skipif. If a certain condition is met skip
     - xfail - the test is expected to fail

     ```python
     from datetime import datetime
     day_of_week = datetime.now().isoweekday()
     
     @pytest.mark.skip
     def test_not_implemented():
       assert False
     
     # will be skipped if the day of week is above 4
     @pytest.mark.skipif('day_of_week > 4')
     def test_something():
       assert something() == True
      
     @pytest.mark.xfail
     def test_fail():
       assert 3 > 4
     ```

6. 







