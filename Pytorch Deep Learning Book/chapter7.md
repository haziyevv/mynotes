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





### Dataloader

This is a pytorch class that is used for minibatching and shuffling the dataset. 

```
train_loader = torch.utils.data.DataLoader(cifar2, 
                                           batch_size=64,
                                           shuffle=True)
```

Shuffle means, shuffle the batch on each epoch. So, a different minibatch will be selected on each epoch.
