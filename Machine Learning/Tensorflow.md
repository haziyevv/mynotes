1. Write the basic import template for tensorflow ?

   ```python
   import os
   os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
   
   import tensorflow as tf
   from tensorflow import keras
   from tensorflow.keras import layers
   
   pysical_devices = tf.config.list_physical_devices("GPU")
   tf.config.experimental.set_memory_growth(pysical_devices[0], True)
   ```

2. How does tensorboard work ?

   ```bash
   tensorboard --logdir=/tmp/model
   ```

   