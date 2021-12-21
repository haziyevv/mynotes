## POS tagging using CRF

1. In **CRF** a set of feature functions are defined to extract features for each word in a sequence.
2. Some examples of feature functions are: **is the first letter of the word capitalised**, **what are the suffix and prefix of the word**, **what is the previous word**. 
3. These set of features are called **State Features**. 
4. We also pass the label of the current and the previous word.
5. Then **CRF** determines the weights of the different feature functions that will maximize the likelihood of the labels on the training data.
6. The feature function dependent on the label of the previous word is called **Transient Feature**.
7. 