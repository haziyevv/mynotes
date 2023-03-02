1. In recurrent neural networks, with increasing the length of the input there was performance degradation. Attention mechanism fixes this.
2. Naradaya-Watson proposed a better approach in which the estimator uses a weighted average where weights correspond to relevance of the training instance to the query: 𝑦ˆ = ∑︁𝑛 𝑖=1 𝛼 (𝑥, 𝑥𝑖)𝑦𝑖 . Here weighting function 𝛼 (𝑥, 𝑥𝑖) encodes the relevance of instance 𝑥𝑖 to predict for 𝑥.
3. Challenged of traditional encoder-decoder:
   1. First, the encoder has to compress all the input information into a single fixed length vector ℎ\_t  that is passed to the decoder.
   2. Second, it is unable to model alignment between input and output sequences, which is an essential aspect of structured output tasks such as translation or summarization
4. The central idea is to induce attention weights 𝛼 over the input sequence to prioritize the set of positions where relevant information is present for generating the next output token
5. Distinctive attention is used when the key and query belong to two distinct input and output sequences
6. 