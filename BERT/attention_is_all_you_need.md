1. What is attention ? 
   
   Before transformer, attention was used to give importance scores for each word in the encoder to the word in the decoder. 
   
   Before attention models were created, in seq2seq models rnn is applied and the final hidden layer of encoder is called **context vector** and sent to the decoder as input. 
   
   1- Send context vector to decoder **2**- calculate hidden layer **3**- find dot product of the hidden layer to each hidden layers in the encoder **4**- find softmax of those dot products **5**-multiply dot product results with corresponding hidden layers and sum **5** - concatenate the result with the hidden layer output of the decoder.   

2. Based solely on attention, dispensing with convolution and recurrence. 

3. Experiments on two machine translation tasks show that these models are superior in quality and are more parallelizable and requires significantly less time to train.

4. **Self-attention** or sometimes called **intra-attention** represents the sequence by relating different positions. Cümlede sözlerin bir birine olan elaqesini gösteren bir vectordur.

5. Self Attention: 

example: The animal didnt cross the street because it was too tired.  

What does "it" refer to in this sentence ? Self attention answers this question. It gives more score to the animal and associates animal and "it".  
