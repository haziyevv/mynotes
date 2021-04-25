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

6. What are continuous, ordinal and categorical values ?
   
   - **Continuous**, is where there is a strict ordering and difference between values has a strict meaning. ex: 1,2,3,4,5,6
   
   - **Ordinal**, is where there is ordering but difference between values has no meaning.  ex: small, medium, large
   
   - **Categorical**, is where there is no ordering and difference between values does not make sense. ex: sport, economy, trade.

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

## 
