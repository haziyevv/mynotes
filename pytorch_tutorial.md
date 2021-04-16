# Deep Learning / ML Basics

- In classical machine learning we were giving features to the model and using that it discriminates between different data and classifies them to different categories. However, in deep learning, the model decides which features to look at and finds out those features that were given by us before.

- This is not to say that feature engineering has no place in deep learning; we often need to inject some form of prior knowledge to deep learning models.

- First important thing about pytorch is it provides multidimensional arrays named tensors with waste amount of operations, and ability to easily move from cpu to gpu. 

- Second important thing is that it uses autograd engine to track the operations on tensors and compute derivatives with respect to any inputs.

- 

- <img title="" src="pytorch_design.jpg" alt="">

**torch.\_\_file\_\_** --> shows the location where torch is installed

## Pretranined networks

#### AlexNet

This architecture was the breakthrough in deep learning. In 2012 ILSVRC competition, ALEXNET won by a large margin or 15% error where second best model which were not using deep learning has got 26% error rate.  The architecture of AlexNet is given below:

<img title="" src="alexnet.jpg" alt="">  

- This model and other famous models are loaded to **torchvision.models** and can easily applied.

- ```
  from torchvision import models
  ```

- When we type dir(models) --> to see the classes and functions in the models a big list will be outputted as given below. There we see capital **AlexNet** and **alexnet**. 
  
  **AlexNet** is the class that we can instantiate, but **alexnet** is the function that returns different models instantiated from those classes. 
  
  ```
  #In: 
  dir(models)
  
  #Out:
  ['AlexNet',
   'DenseNet',
   'GoogLeNet',
   'GoogLeNetOutputs',
   'Inception3',
   'InceptionOutputs',
   '__package__',
   '__path__',
   '__spec__',
   '_utils',
   'alexnet',
   'densenet',
   'densenet121',
   'densenet161',
   'mobilenet_v3_large',
   'resnet18',
   'resnet34',
   'resnet50',
   'shufflenetv2',
   'vgg13_bn',
   'vgg16',
   'wide_resnet50_2']
  ```

If we type **models.AlexNet(**) we will get an empty AlexNet class. We should train it from scratch or load weights. However, lower case **alexnet** --> function is equipped with the argument that we can pass to make the model load pretrained weigths.

```
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

- Python lists or tupples are collections of Python objects that are individually allocated into memory. Pytorch tensors or NumPy arrays on the other hand are views over contiguous memory blocks. Pytorch or numpy arrays are unboxxed C numeric types not python objects.

- 
