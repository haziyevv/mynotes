1. To make and or operations in numpy:

   ```python
   import numpy as np
   
   a1 = np.array([1,32,2,4,5,6,7,8])
   
   # if you do this: it will throw error
   a1 > 12 and a1 < 20
   
   # instead:
   np.logical_and(a1 > 12, a1 < 20)
   np.logical_or(a1 > 12, a1 < 20)
   ```

2. To create a random number:

   ```python
   import numpy as np
   
   np.random.rand()
   ```

3. In order to get the same random number in each run:

   ```python
   import numpy as np
   
   np.random.seed(1)
   np.random.rand()
   ```

4. To randomly generate an integer from a given interval:

   ```python
   import numpy as np
   
   np.random.seed(1)
   np.random.randint(1,10) # will generate a random number between 1 and 10
   ```

   ```python
   # Import numpy and set seed
   import numpy as np
   np.random.seed(123)
   
   # Use randint() to simulate a dice
   print(np.random.randint(1,7))
   
   # Use randint() again
   print(np.random.randint(1,7))
   
   # In this scenario two different random variables will be generated because for the first call seed is created only. 
   
   # If you want to get same result, do this:
   np.random.seed(123)
   print(np.random.randint(1,7))
   
   np.random.seed(123)
   print(np.random.randint(1,7))
   ```

5. 