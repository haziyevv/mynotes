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
