## RASA
1. In Rasa NLU user can choose between two components:
    1. Pretrained embeddings (sklearn)
    2. Supervised Embeddings (tensorflow)

2. Pretrained Embeddings (intent classifier sklearn): Uses spacy to load pretrained language models, to use as word embeddings.
    1. This word embeddings are specific to language. **You have to chose different models depending on the language you are using**
    2. RASA NLU takes the average of all word embeddings within a message, and then uses support vector classifier.  
    3. Grid search is applied to find the optimal hyper parameters

3. Supervised Embeddings (intent classifier tensorflow): 
    1. Instead of using pretrained embeddings, it trains the embeddings from scratch.
    2. **Supports multiple intents**
    3. 
 
4. Can I specify more than one intent classification model in my pipeline?
    - Technically yes, but there is no real benefit. The predictions of the last specified intent classification model will always be what’s expressed in the output.



## DIET model
1. Take both embedding of the token using **pretrained embeddings** and sparse features (one hot encoding of the word, character ngrams)
2. Mask some tokens in the input text



## STARSPACE
1. Meaning of the input text should be similar to the meaning of the label
If the tag and the input text has embeddings, they should be similar. 


