1. **Functional API** -  Pytorch has functional counterparts for each nn module. Meaning there are **torch.nn.functional.linear, torch.nn.functional.conv2d, torch.nn.functional.tanh etc**. available. These are functions that you give parameters and it returns value. In best practice it is better to replace **nn.MaxPool2d with F.maxpool2d(), nn.Tanh with F.tanh()** etc, which does not require parameters to manage and recognize.

## Regularization

- L2 Regularization or weight decay regularization:

```
l2_lambda = 0.001
l2_norm = sum(p.pow(2.0).sum() for p in model.parameters())
loss = loss + l2_lambda*l2_norm
```

* Dropout: add nn.Dropout() module between the nonlinear activation function and the linear or convolutional module of the subsequent layer. 
