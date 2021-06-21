1. What is Perplexity ?

The standard evaluation method for calculating Language Models. Low perplexity is better.

<img title="" src="file:///home/haziyevv/Documents/mynotes/figures/perplexity.png" alt="">

For example:

Mene deniz verin



$$
(\frac{1}{P(Mene)} * \frac{1}{P(deniz|Mene)} * \frac{1}{P(verin|Mene \ deniz)})^1/_3
$$





2. **LSTM:**
- On step t, there is both a hidden state **h\_t** and cell state **c\_t**. 

- Cell state is used to store long-term informarion. 

- LSTM can erase, write and read information from the cell.

-  Erase, write and read information are controlled by 3 different gates.

- 






















