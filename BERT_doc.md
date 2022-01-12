# Transformers

1. Starts with a **Positional Encoder**
2. Then follows a **Multihead Attention**. There are 8 **self attentions** inside multihead attention. Takes the average of those attentions
3. Decoder: 
   - **Positional Encoder** --> 
   - **Masked Multihead Attention** --> we should mask the words in the decoder coming after the given word, because we should not know what is coming after the given word. 
   - **Multihead Attention**



# BERT

1. Bidirectional Encoder Representation for Transformers

2. **Pretraining**: Learn what is language ? and what is the context?

3. **BERT** learns language by training on two unsupervised tasks simultaneously:

   - Masked Language Modelling
   - Next Sentence Prediction

4. **Masked Language Modeling**: BERT takes sentence, where random words are replaced with **[MASK]** . The goal is to output this masked tokens. 

   The [MASK1] brown fox [MASK2] over the lazy dog

   [MASK1] --> quick  [MASK2] --> jumped

5. **Next Sentence Prediction**: BERT takes in two sentences and determines if the second sentence actually follows the first. More like a **binary classification** problem.

6. In **Pretraining** Masked Language Modelling and Next Sentence Prediction are done together. 

7. We feed **Masked Sentence A** and **Masked Sentence B** to the model. In the output we return one binary output for the **NSP** (1 if sentence B follows sentence A, 0 if not). Also word vectors are outputed as the number of words inputed.

8. Open AI's GPT2 model also uses transformer and builds a language model but it is one directional

9.  

