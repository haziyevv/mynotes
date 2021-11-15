1. Import modules

```python
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time
```



2. Download the text file of shakespeare text.

```python
path_to_file = tf.keras.utils.get_file('shakespeare.txt', url)
```

3. 

```python
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))
```

