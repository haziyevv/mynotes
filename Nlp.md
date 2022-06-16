[TOC]



# What is Perplexity ?

The standard evaluation method for calculating Language Models. Low perplexity is better.

<img title="" src="file:///home/haziyevv/Documents/mynotes/figures/perplexity.png" alt="">

For example:

Mene deniz verin



$$
(\frac{1}{P(Mene)} * \frac{1}{P(deniz|Mene)} * \frac{1}{P(verin|Mene \ deniz)})^1/_3
$$





# **LSTM:**

- On step t, there is both a hidden state **h\_t** and cell state **c\_t**. 
- Cell state is used to store long-term informarion. 
- LSTM can erase, write and read information from the cell.
- Erase, write and read information are controlled by 3 different gates.



# Transformers
1. Consists of **N** encoders. The output of one encoder is sent as input to the encoder above it. The final encoder returns the representation of the given source sentence as output.
2. 
3. Starts with a **Positional Encoder**
4. Then follows a **Multihead Attention**. There are 8 **self attentions** inside multihead attention. Takes the average of those attentions
5. Decoder: 
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



## Structure

Self Attention: 



# Huggingface Notes

1. Transformer models can be grouped into three categories:
* GPT-like (auto-regressive transformer models)

* BERT-like (auto-encoding transformer models)

* BART/T5 - like (sequence-to-sequence Transformer models)
2. Encoder Models --> BERT, ALBERT, DistilBERT
* This models use only encoder part of the transformer model. 

* This works bertter for Natural Language Understanding tasks, like Sentiment Analysis, Text Classification, Named Entity Recognition etc.
3. Decoder Models --> GPT, GPT2 etc. 
* This models use only decoder part of the transformer model.

* Works better for Natural Language Generation tasks. Predicting the next word given some words. 
4. Encoder-decoderr models --> BART, T5 etc.

5. Uses both encoder and decoder parts of the transformer model.

6. Works better for seq2seq problems, like summarization and translation.

7. 

















