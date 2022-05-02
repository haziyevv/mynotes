1. **tf.constant** - produces constant tensors

   **tf.Variable** - produces tensors that can be modified
   
2. How to change the shape of a tensor ?

   ```python
   x = tf.constant([[3, 5, 2], [7, 6, 8]])
   
   y = tf.reshape(x, [3, 2])
   ```

3. How to create a variable ?

   ```python
   x = tf.Variable(2.0, dtype=tf.float32, name='my_variable')
   ```

4. **GradientTape** records operations of variables for automatic differentiation like in autograd.

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



## Input Pipeline

1. Links: https://www.tensorflow.org/guide/data (input pipeline guide)

2. To construct a `Dataset` from data in memory use `tf.data.Dataset.from_tensors()` or `tf.data.Dataset.from_tensor_slices((X, Y))`. This means it will remove the first dimension of the input array. If its shape is (2,5) then we will get 2 vectors with shape (5,). If its shape is (2,4,5), then we will get 2 tensors with shape (4,5).

3. How to divide a dataset to batches ?

   ```python
   dataset = tf.data.Dataset.from_tensor_slices(X, Y)
   dataset = dataset.batch(batch_size=16)
   ```

4. If you want to have exact same number of elements in each batch, then you should drop the last batch, because it may have elements less than the batch_size:

   ```python
   dataset = dataset.batch(batch_size=16, drop_remainder=True)
   ```

5. Once you have dataset, you can transform in into a new `Dataset`.  You can both apply per-element transformation with `Dataset.map()` and multi-element transformations with `Dataset.batch()`.

6. If you want to batch a variable shape dataset use:

   ```python
   ds_series_batch = ds_series.shuffle(20).padded_batch(10)
   ```

6. **TextLineDataset** is used to read from one csv file:

   ```python
   dataset = tf.data.TextLineDataset([file_path1, file_path2])
   dataset = dataset.map(some_parse_method)
   ```
   
   
   
8. How to read from several csv files:

   ```python
   dataset = tf.data.experimental.make_csv_dataset(file_pattern='../data/*.txt', 
                                                   batch_size=2, 
                                                   column_names=CSV_COLUMNS,
                                                   column_defaults=DEFAULTS)
   ```

   file_pattern: list of files or patterns of file paths containing csv records

   CSV_COLUMNS = [
       'utterance',
       'intents',
   ]


   DEFAULTS = [['na'], ['na']]

7. 









2. How to apply **k-fold cross validation** in keras ?

   ```python
   from tensorflow.keras.wrappers.scikit-learn import KerasClassifier
   from sklearn.model_selection import cross_val_score, KFold
   
   def build_model():
   	model = Sequential()
   	model.add(Dense(1, input_shape=(1,), activation="sigmoid"))
       model.compile(optimizer=Adam(learning_rate=0.3),
                     loss="binary_crossentropy",
       			  metrics="accuracy")
       return model
   
   model = KerasClassifier(build_fn=build_model, epochs=25)
   cv = KFold(3, shuffle=True)
   scores = cross_val_score(model, X, y, cv=cv)
   ```





# TF feature_column

1. **tf.feature_column** consists of methods to represent features in different ways.

   - **tf.feature_column.numeric_column**: 

   ```python
   feature_columns = []
   
   lattitude = tf.feature_column.numeric_column("lattitude")
   feature_columns.append(lattitude)
   
   longitude = tf.feature_column.numeric_column("longitude")
   feature_columns.append(longitude)
   
   # to convert the list of feature columns into a layer, that will be part of a model
   fp_feature_layers = layers.DenseFeature(feature_columns)
   ```

   - **tf.feature_column.bucketized_column**:

   ```python
   feature_columns = []
   
   latitude_as_a_numeric_column = tf.feature_column.numeric_column("latitude")
   latitude_boundaries = list(np.arange(int(min(train_df["latitude"])),
                                        int(max(train_df["latitude"])),
                                        1))
   
   latitude = tf.feature_column.bucketized_column(latitude_as_a_numeric_column,
                                                  latitude_boundaries)
   feature_columns.append(latitude)
   ```

   - **tf.feature_column.crossed_column**: crossed lattitude and longitude features to create a new feature. If there are 10 lattitude and 10 longitude classes, the dimension of new feature will be 100.

   ```python
   latitude_x_longitude = tf.feature_column.crossed_column([latitude, longitude], hash_bucket_size=100)
   ```

   - **tf.feature_column.indicator_column**: creates one hot encoded features

   ```python
   crossed_feature = tf.feature_column.indicator_column(latitude_x_longitude)
   ```



## Keras Preprocessing

1. **Categorical Features**:

   - **tf.keras.layers.CategoryEncoding**: Turns integer categorical features into one-hot, multi-hot or count-dense representations
   - **tf.keras.layers.hashing**:  Performs categorical feature hashing
   - **tf.keras.layers.StringLookup**: Turns string categorical values into an encoded representation that can be read by an **Embedding** or dense layer. 
   - **tf.keras.layers.IntegerLookup**: Turns integer categorical values into and encoded representation that can be read by an **Embedding** or **dense** layer.

2. Transforms a batch of texts to numerical indices. This could be fed to embedding layer or a dense layer.

   ```python
   tf.keras.layers.TextVectorization()
   ```











## Sequential API

2. How to get the list of all layers in the model ?

   ```python
   model.layers
   model.layers[1].name #gives the name of the layer
   model.get_layer('dense_3').name  #gives the name of the dense_3 layer
   model.layers[1].get_weigths() # gets all the weights in the given layer
   
   ```

3. Using **history** we can **plot** the performance of the model:

```python
history = model.fit(x_train, y_train, epochs=30,
					validation_data=(x_valid, y_valid))

pd.DataFrame(history.history).plot(figsize=(8,8))
```

![history_plot](/home/haziyevv/Documents/mynotes/figures/history_plot.png)



3. How to call **callback** to save the model after each epoch ?

```python
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5") 
history = model.git(x_train, y_train, epochs=30,
					validation_data=(x_valid, y_valid),
					callbacks=[checkpoint_cb])
```

If you want to save the **best model** :

```python
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5",
												save_best_only=True) 
```



4. How to apply **early stopping** in training ?

```python
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10,
												  restore_best_weights=True)

history = model.fit(x_train, y_train, epochs=30,
                   	validation_data=(x_val, y_val),
                    callbacks=[checkpoint_cb, early_stopping_cb])
```

5. How to write **custom callback** to display the ratio between the validation and training loss **after each epoch end**?

```python
class PrintValTrainRatiocallback(keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs):
        print("\nval/train: {:.2f}".format(logs["val_loss"]/logs["loss"]))
```

6. How to load to tensorflow dataset from dataframe ?

```python
train_data = tf.data.Dataset.from_tensor_slices((train_df["question_text"].values, train_df["target"].values))
valid_data = tf.data.Dataset.from_tensor_slices((validation_df["question_text"].values, validation_df["target"].values))
```



7. How to load text data from directory to tensorflow dataset ?

   ```python
   raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
       'folder_name',
       batch_size=batch_size,
       validation_split=0.2,
       subset='validation',
       seed=seed)
   ```

8. How to download data from a url to cache ? 

   ```python
   tf.keras.utils.get_file(fname="filename", origin=url,
                          untar=True,cache_dir=".",
                          cache_subdir="")
   ```

9. 

