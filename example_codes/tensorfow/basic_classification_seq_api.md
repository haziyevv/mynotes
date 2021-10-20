```python
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt

train_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
test_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_test.csv")
train_df = train_df.reindex(np.random.permutation(train_df.index)) # shuffle the training set

# normalise data
tr_mean = train_df.mean()
tr_std = train_df.std()
test_std = test_df.std()
test_mean = test_df.mean()
train_df_norm = (train_df - tr_mean)/tr_std
test_df_norm = (test_df - test_mean)/test_std

threshold = 260000
train_df_norm["median_house_value_is_high"] = train_df["median_house_value"].apply(lambda x: 1 if x > threshold else 0)
test_df_norm["median_house_value_is_high"] = test_df["median_house_value"].apply(lambda x: 1 if x > threshold else 0)

feature_columns = []
median_income = tf.feature_column.numeric_column("median_income")
total_rooms = tf.feature_column.numeric_column("total_rooms")
feature_columns.extend([median_income, total_rooms])
feature_layer = layers.DenseFeatures(feature_columns)

def create_model(lr, feature_layer, mtrcs):
    model = models.Sequential()
    model.add(feature_layer)
    model.add(layers.Dense(1, input_shape=(1,), activation=tf.sigmoid))
    model.compile(optimizer=RMSprop(learning_rate=lr), 
                  loss=keras.losses.BinaryCrossentropy(),
                  metrics=mtrcs)
    return model
    
def train_model(model, dataset, label_name, bs, epc, shfl=True):
    features = {key:np.array(value) for key,value in dataset.items()}
    label = np.array(features.pop(label_name))
    
    history = model.fit(x=features, y=label, batch_size=bs, 
                        epochs=epc, shuffle=shfl)
    epochs = history.epoch
    hist = pd.DataFrame(history.history)
    
    return epochs, hist
    
def plot_curve(epochs, hist, list_of_metrics):
    plt.figure()
    plt.xlabel("Epoch")
    plt.ylabel("Value")
    
    for m in list_of_metrics:
        x = hist[m]
        plt.plot(epochs[1:], x[1:], label=m)
    plt.legend()
    
learning_rate = 0.001
epochs = 20
batch_size = 100
label_name = "median_house_value_is_high"
classification_threshold = 0.35

METRICS = [keras.metrics.BinaryAccuracy(name='accuracy', 
                                           threshold=classification_threshold),
           keras.metrics.Precision(thresholds=classification_threshold,
                                           name='precision'),
           keras.metrics.Recall(thresholds=classification_threshold,
                                           name='recall')]

my_model = create_model(learning_rate, feature_layer, METRICS)
epochs, hist = train_model(my_model, train_df_norm, label_name,
                           batch_size, epochs)
list_of_metrics_to_plot = ['accuracy', 'precision', 'recall'] 

plot_curve(epochs, hist, list_of_metrics_to_plot)
```

