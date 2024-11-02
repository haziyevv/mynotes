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

2. 