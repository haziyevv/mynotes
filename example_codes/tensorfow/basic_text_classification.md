1. Import needed packages

```python
import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
```



2. Download the necessary sentiment analysis data. It consists of text with their label positive or negative.

```python
url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
tf.keras.utils.get_file(fname="aclImdb", origin=url, untar=True, cache_subdir="", cache_dir=".")
```



3. Create train, validation and test datasets from the given directory.

```python
raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory("aclImdb/train", batch_size=32, validation_split=0.2, subset="training", seed=42)
raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory("aclImdb/train", batch_size=32, validation_split=0.2, subset="validation", seed=42)
raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory("aclImdb/test", batch_size=32)
```



4. Vectorize the train, validation and test dataset.

```python
max_tokens = 10000
sequence_length = 250

vectorize_layer = tf.keras.layers.TextVectorization(max_tokens=max_tokens,                                                output_sequence_length=sequence_length) 

# make a text only dataset and adapt
train_text = raw_train_ds.map(lambda x,y: x)
vectorize_layer.adapt(train_text)

def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label

  
train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)
```



5. Configure for better performance. 

```python
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)
```



6. Create the training model.

```python
embedding_dim = 16

model = tf.keras.Sequential([
  layers.Embedding(max_features + 1, embedding_dim),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(1)])

model.summary()
```



7. Train the model

```python
model.compile(loss=losses.BinaryCrossentropy(from_logits=True),
              optimizer='adam',
              metrics=tf.metrics.BinaryAccuracy(threshold=0.0))

epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs)
```

