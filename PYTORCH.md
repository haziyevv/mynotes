# Deep Learning / ML Basics

- First important thing about pytorch is it provides multidimensional arrays named tensors with waste amount of operations, and ability to easily move from cpu to gpu. 

- Second important thing is that it uses autograd engine to track the operations on tensors and compute derivatives with respect to any inputs.

- **torch.\_\_file\_\_** --> shows the location where torch is installed


- Famous models are loaded to **torchvision.models** and can easily applied.

  ```
  from torchvision import models
  ```

- When we type dir(models) --> to see the classes and functions in the models a big list will be outputted. There we see capital **AlexNet** and **alexnet**. 

  **AlexNet** is the class that we can instantiate, but **alexnet** is the function that returns different models instantiated from those classes. 

  If we type **models.AlexNet(**) we will get an empty AlexNet class. We should train it from scratch or load weights. However, lower case **alexnet** --> function is equipped with the argument that we can pass to make the model load pretrained weigths.
  
  

```python
alexnet = models.alexnet(pretrained=True)
```

Just **alexnet(input)** --> will give us 1000 dimension vector, which is the vector defining scores for 1000 different classes. In alexnet it is trained with **imagenet** data and output consists of 1000 different objects. 

Before we should apply preprocessing. 

```
from torchvision import transforms

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.3,0.2,0.4], 
                         std=[0.2,0.1,0.2])
])
```

After going through preprocess, we can send our data to the **alexnet** as input.





## Pytorch Tensors

- Pytorch tensors are similar to numpy arrays but with a few additional superpowers. 

  - Ability to perform operations on GPU

  - Distribute operations to multiple devices

  - Keep track of the graph of computations that created them

A simple one dimensional tensor with ones.

- ```
  import torch
  a = torch.ones()
  
  In [4]: a
  Out[4]: tensor([1., 1., 1.])
  ```

###### Essense of Tensors

- Python lists or tupples are collections of Python objects that are individually allocated into memory. Pytorch tensors or NumPy arrays on the other hand are views over contiguous memory blocks. Pytorch or numpy arrays are unboxed C numeric types not python objects.

```
points = torch.tensor([[5,3,2], [4,3,3]])

In [3]: points
Out[3]: 
tensor([[5, 3, 2],
        [4, 3, 3]])



In [4]: points[0]
Out[4]: tensor([5, 3, 2])
```

Here we created a tensor object and then accessed the first row of that object. Does this mean we have created a new tensor object ? Of cource not, the object is the same in the storage but a view of that storage is returned.





### Tensor element types

1) Numbers in python are objects, but in numpy they are just 32 bit floating point numbres. İn python lists, python convert the number to an object with different capabilities that need more memory. 
2) Python interpreter is slow compared to a compiled code.
3) Data types:

   1) torch.float32 --> default data type for tensors. 32 bit floating point number

   2) torch.float16 --> half precision floating-point number

   3) torch.int64 --> or torch.long , singned 64 bit integers
4) Default data type for floating point numbers is torch.float32 and for integers is torch.int64 



### Torch Storage

1) Values in tensors are allocated to contiguous chunks of memory managed by **torch.Storage.** 

2) **torch.Storage** is a one dimensional array. 

3) A pytorch tensor instance is a view of that storage, that can acces to the storage using **offset** and **per dimension strides**. 

```
In [49]: points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])

In [50]: points
Out[50]: 
tensor([[4., 1.],
        [5., 3.],
        [2., 1.]])



In [51]: points.storage()
Out[51]: 
 4.0
 1.0
 5.0
 3.0
 2.0
 1.0
[torch.FloatStorage of size 6]
```

In the code above points tensor has a shape (3,2) but the storage is one dimensional. 

If you change the value in storage, it will also changed in the given tensor object.

```
stor = points.storage()
In [61]: stor
Out[61]: 
 4.0
 1.0
 1.0
 3.0
 2.0
 1.0


In [62]: stor[3] = 7

In [63]: points
Out[63]: 
tensor([[4., 1.],
        [1., 7.],
        [2., 1.]])
```





#### Tensor metadata: Size, offset and stride

1) size is the size of tensor in each dimension

```
In [69]: points.size()
Out[69]: torch.Size([3, 2])
```

2. Storage offset is the index in the storage corresponding to the first element of  the tensor.

```
In [70]: points.storage_offset()
Out[70]: 0
```

3. Stride is the number of elements in the storage that need to be skipped to obtain the next element along each dimension.

```
In [71]: points.stride()
Out[71]: (2, 1)
```

4. When get a part of the points tensor using index, a new storage will not be allocated, it will still use the same storage but its storage offset and stride will change.

```
second_point = points[1]

In [75]: second_point.storage_offset()
Out[75]: 2


In [76]: second_point.stride()
Out[76]: (1,)
```

If we change respective numbers in the **storage**, then both **second_point** and points **tensors** will also change.

Also, if we change the **second_point** tensor, both **storage** and **points** tensor will also change.

5. If we take transpose, again the storage will not change but the stride and shape will change.

```
In [129]: points_t = points.t()In [130]: points_tOut[130]: tensor([[4., 5., 2.],        [1., 3., 1.]])In [131]: id(points_t.storage()) == id(points.storage())Out[131]: TrueIn [133]: points.stride()Out[133]: (2, 1)In [134]: points_t.stride()Out[134]: (1, 2)
```

6. When we take the transpose and create **points_t**, then it will not be a contiguous tensor. 

```
In [135]: points_t.is_contiguous()Out[135]: False
```

7. To make it contiguous again:

```
points_t = points_t.contiguous()
```

In the contiguous tensors number are alligned to the storage row by row.



### Moving Tensors to GPU

1. A tensor can be created in gpu directly.

```
points = torch.tensor([[5,3,2], [4,4,2], [4,3,3]], 
                        dtype=torch.float32, 
                        device="cuda")
```

2. Also it can be moved from cpu to gpu and vice versa.

```
points = points.to("cpu")
```





## **Serializing Tensors**

1. To save and load as pickle. Disadvantage of this is that we can only load this with PyTorch.

```
torch.save(points, "test.t")

points = torch.load("test.t")
```

2. Serialize using hdf5. 

```
f = h5py.File("file.hdf5", "w")
dset = f.create_dataset("coord", data=points.numpy())
f.close()
```





## Data Representation

1. What data type each scalar representing a pixel is is encoded generally in consumer cameras?

   - Using 8 bit integers

   - In some medical, scientific and industrial applications, you can find 12bit or 16bit

2. How to load an image using imageio?

```
import imageio
img_arr = imageio.imread("filename.jpg")
In [13]: img_arr.shape
Out[13]: (1280, 960, 3)
```

3. What is the layout pytorch modules dealing with images require tensors to have?

   - **CxHxW** --> channel, height, witdh

   - in the example above the picture has shape **HxWxC**. So it should be converted to the accepted format.

4. How to correct the layout from **HxWxC** to **CxHxW** ?

```
In [10]: img_arr = img_arr.permute(2, 0, 1)

In [11]: img_arr.shape
Out[11]: torch.Size([3, 1280, 960]
```

5. What is the layout to store multiple images in a batch of arrays ? 

   - **NxCxHxW** --> number of images, channels, height, width




### Normalizing image data

1. Just divide the values of the pixels to 255, this is a little bit naive

   ```
   batch = batch.float()
   batch /= 255.0
   ```

2. Compute mean and standars deviation and normalise to have zero mean and unit standard deviation.

```
n_channels = batch.shape[1]
for c in range(n_channels):
    mean = torch.mean(batch[:, c])
    std = torch.std(batch[:,c])
    batch[:,c] = (batch[:,c]-mean)/std
```





### 3D images

1. Images we talked before are 2d images that are taken with a camera. In some contexts such as medical imaging, for example CT (computer tomography), we deal with sequences of images stacked from head to foot axis. 

2. In CT scans intensity is used instead of channel. 

3. Intensity represents the density of different body parts. 

4. CTs have only a single intensity channel, like a grayscale image. 

5. Layout of CT scan image : **NxCxDxHxW** --> batch size, channel, depth, height, width

**Scatter Method**:  Fills the tensor with values from a source tensor along the indices provided as arguments. 

```
target_onehot = torch.zeros(5, 4)
target = torch.tensor([2,1,1,3,2])

In [24]: target_onehot.scatter(1, target.unsqueeze(1), 1)
Out[24]: 
tensor([[0., 0., 1., 0.],
        [0., 1., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 0., 1.],
        [0., 0., 1., 0.]])
```

first argument to scatter method is the dimension in which to add number, 

second argument is indices of the elements to scatter,

third argumnet is the number to put.

1. What does **unsqueeze** do ?

   - increases the dimension of the tensor in the given axis





## Broadcasting

* Ability to apply operations on matrices with different sizes. There are some constraints.

1) Two dimensions are compatible when they are equal or one of them is one.

2) If the number of dimensions of matrix 1 and matrix 2 are not equal, then prepend ones to the dimension of tensor with fewer dimensions.

3) Broadcasting does not apply to inplace operations

```
a = torch.ones(3,1,2)
b = torch.ones(1,8,1)

c = a*b
c.shape
(3, 8, 2)
```





## Autograd

1. Params -> variables are started with **requires_grad=True** . Which means their calculation will be memorized and in each backward their derivatives will be **accumulated**. 

   1. To stop accumulation, **params.grad.zero()** should be called in each iteration. 

   2. when updating params, stop the autograd then start again, using with **torch.no_grad().**

```
    for epoch in range(epochs):
        if params.grad is not None:
            params.grad.zero_()
        y_hat = model(x, *params)
        loss = loss_fn(y_hat, y)
        loss.backward()
        with torch.no_grad():
            params -= (learning_rate * params.grad)
```





### Optimizer -->

Used to update the parameters automatically and apply all kinds of learning rate adaption and optimization strategies.

Code above will be decrease like this:

```
    optimizer = optim.SGD(params=[params], lr=learning_rate)
    for epoch in range(epochs):
        t_p = model(t_un, *params)
        loss = loss_fn(t_p, t_c)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

**loss.backward** calculates the derivatives of all the parameters and **optimizer.step** updates those parameters using the given calculated derivatives. 

**Stochastic Gradient Descent:** The gradient is obtained by averaging a random minibatch from the whole dataset. 

1. What does  torch.set_grad_enabled(True) do ?

```
def calc_forward(x, y, is_train):
    with torch.set_grad_enabled(is_train):
        y_hat = model(x)
        loss = loss_fn(y_hat, y)

    return loss
```

Here we apply one forward pass for either training or validation. If we want validation we should select **is_train=False**. For training **is_train = True**.





## Basic Neural Network

```
import torch.nn as nn
import torch.optim as optim
```

1. Sequential Model --> a model consisting of several layers.

```
seq_model = nn.Sequential(
                nn.Linear(1, 13),
                nn.Tanh(),
                nn.Linear(13, 1))
```

2. To see the shapes of parameters:

```
[param.shape for param in seq_model.parameters()]

[torch.Size([13, 1]),
 torch.Size([13]), 
torch.Size([1, 13]), 
torch.Size([1])]
```

3. To see the shapes of parameters with their names:

```
[(name, param.shape) for name, param in seq_model.named_parameters()]


[('0.weight', torch.Size([13, 1])), 
('0.bias', torch.Size([13])), 
('2.weight', torch.Size([1, 13])), 
('2.bias', torch.Size([1]))]
```

4. In pytorch as you can see from the figure below and from the shapes given before,  one bias is added for each node.

<img title="" src="/home/haziyevv/Documents/mynotes/figures/bias.jpg" alt="">

the NN model is 1 -- 13 -- 1. Bias shapes are 13 and 1. One bias for each node. 

5. We can also give name to each layer like this:

```
seq_model = nn.Sequential(OrderedDict([
    ("hidden_linear", nn.Linear(1, 13)),
    ("hidden_activation", nn.Tanh()),
    ("output_linear", nn.Linear(13, 1))
])
```

output will be like below. This is more readable and easy to understand.

```
[('hidden_linear.weight', torch.Size([13, 1])), 
('hidden_linear.bias', torch.Size([13])), 
('output_linear.weight', torch.Size([1, 13])), 
('output_linear.bias', torch.Size([1]))]
```





## Torchvision Module

1. How to download CIFAR10 dataset using torchvision datasets and divide it to training and validation ?

```
from torchvision import datasets
cifar10 = datasets.CIFAR10("data_path", train=True, download=True)
cifar10_val = datasets.CIFAR10("data_path", train=False, download=True)
```

- first argument is  where to download the data. 

- second argument is if it is a training or validation data. train=True will get us training data and train=False will get validation data.

- third argument is if we should download if it does not exist in the given folder.

2. How to see the method resolution order of cifar10 instance ?

```
type(cifar10).__mro__

(torchvision.datasets.cifar.CIFAR10,
 torchvision.datasets.vision.VisionDataset,
 torch.utils.data.dataset.Dataset,
 typing.Generic,
 object)
```

3. How to do transform PIL images to torch tensors ? 

```
from torchvision import transforms

to_tensor = transforms.ToTensor()
img_t = to_tensor(img)
```

- This can be added to when the data is get using datasets.cifar10

```
cifar10 = datasets.CIFAR10("data_path", 
                           train=True, 
                           download=True,
                           transform=transforms.ToTensor())
```

this way downloaded dataset will be in torch tensor format and its data type will be converted from int8 to float32 and numbers will range from 0 to 1.

- We can also do this:

```
cifar10.transform = transforms.ToTensor()
```

4. How to normalize data using torch.transforms ?

It is a good practice to normalize the dataset to that each **channel** has  zero mean and unit standard deviation. **torch.transforms.Normalize** can be used here but standard deviation and mean values should be calculated beforehand.



```
imgs = torch.stack([img_t for img_t, _ in tensor_cifar10], dim=3)
```

In this line of code we are stacking the images on third dimension. Each image has (3, 32, 32) shape. Imgs tensor will have (3, 32, 32, 50000) shape, as imgs will be stacked on third dimension.

```
mean = imgs.view(3, -1).mean(dim=1)
std = imgs.view(3, -1).std(dim=1)
```

In this line mean for each channel is calculated. What .view() does? 

view changes the shape from 3,32,32,50000 to 3, 32\*32\*50000. Then we can calculate for each channel. 



- Calculated mean and standard deviation are used for normalisation. To apply both totensor and normalisation operations torch.transforms.Compose is used.

```
transformed_cifar10 = datasets.CIFAR10("path", train=True, download=True,
                                       transform=torch.Compose([
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean, std))
                                       ]))
```



- Which one should we prefer MSE (mean square error) or NLL(negative log likelihood) loss function for classification task ?

  - MSE does not work on classification, although it is best for regression. Because its main objective is to converge output to the given values. So in classification just finding the correct result is enough, it does not need to have 100% probility.





- What is the difference between NLL and Cross entropy ?

**Cross Entropy calculation:**

  loss = - $\sum$ t_i \* log(p_i)   --> here t_i is the true value of the class i and p_i  is the predicted value. 

**Negative Likelihood calculation**:

loss = - $\sum$ log(p_i)

As we can predict, in classification problems, both cross entropy and NLL gives the same results, because, t_i value is only 1 in the correct class and zero in any other class.

Also in pytorch, **nn.NLLLoss()** does not take the logarithm of the output, it just sums the probabilities and expects log probabilities as input. For this reason another **nn.LogSoftmax** layer is added to the end of the Neural Network model. However, on **nn.CrossEntropyLoss()** you just give the output logits ass input to the loss function at it will give the same result. This is better as no need for extra **nn.LogSoftmax()** layer in the Neural Network model.





## Dataloader

This is a pytorch class that is used for minibatching and shuffling the dataset. 

```python
train_loader = torch.utils.data.DataLoader(cifar2,                                            batch_size=64,                                           
										   shuffle=True)
```

Shuffle means, shuffle the batch on each epoch. So, a different minibatch will be selected on each epoch.



# Medical ML

**Voxel**: 3d equivalent of a pixel. Arranged in a 3d grid to represent a field of data. Each **Voxel** of a **CT** scan corresponds to the average mass density of the matter contained inside.  High density material like **bones and metal implants** will be shown as **white**, low density **air and lung tissue** as **black** and fat and tissue as various shades of gray.

End to end solution process:

1) Load CT data files to produce a CT instance that contains the full 3D scan.

2) Identify voxels of potential tumors. Like a heatmap.

3) Group the interesting voxels into small **lumps**.

4. Identify nodules. Classify candidate nodules as a nodule or not.  

5. Find if the nodules are actually malignant. 

**Tumor** : Mass of tissue made of proliferating cells in the lung is a tumor.

**Nodule:** A small tumor (just a few millimeters wide) in the lung is called a nodule. 

4. **DICOM** --> native file format for ct scans.

5. **Hounsfield scale** quantitative scale used for radiodensity. Frequently used on ct scans. 
