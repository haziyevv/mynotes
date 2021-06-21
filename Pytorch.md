# Pytorch

## Data Loaders

1. It supports **map-style** and **iterable-style** datasets

2. Customize data loading order

3. Automatic Batching

4. Single and Multi Process data loading

5. Automatic memory pinning



### Dataset Types:

Map-style Datasets and Iterable Style Datasets

1. Map style Datasets ?

Implements \_\_getitem\_\_ () and \_\_len\_\_() and you can acces an item from dataset using its idx.

2. Iterable style Datasets ?

Implements \_\_iter\_\_(). Most useful when data is coming from a stream. 



### Data loading order and Sampler:

1. 


