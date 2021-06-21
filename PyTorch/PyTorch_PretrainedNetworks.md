# PyTorch Pretrained networks

1) **torch.__file__** --> shows the location where torch is installed

**AlexNet**

This architecture was the breakthrough in deep learning. In 2012 ILSVRC competition, ALEXNET won by a large margin or 15% error where second best model which were not using deep learning has got 26% error rate. The architecture of AlexNet is given below:

<img title="" src="figures/alexnet.jpg" alt="">  

- This model and other famous models are loaded to **torchvision.models** and can easily applied.

- ```
  from torchvision import models
  ```
* When we type dir(models) --> to see the classes and functions in the models a big list will be outputted as given below. There we see capital **AlexNet** and **alexnet**.

* **AlexNet** is the class that we can instantiate, but **alexnet** is the function that returns different models instantiated from those classes.

* ```
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

* If we type **models.AlexNet(**) we will get an empty AlexNet class. We should train it from scratch or load weights. However, lower case **alexnet** --> function is equipped with the argument that we can pass to make the model load pretrained weigths.
  
  ```
  alexnet = models.alexnet(pretrained=True)
  ```

* Just **alexnet(input)** --> will give us 1000 dimension vector, which is the vector defining scores for 1000 different classes. In alexnet it is trained with **imagenet** data and output consists of 1000 different objects.
  
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
