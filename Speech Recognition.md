## Problems needed to solve to apply ASR



1. Convert the analog signal (acoustic wave) to digital representation

2. Seperate the signal from noice. Meaning, someone is talking --> this is the signal, but there are other people also talking in background or a phone ringing --> these are the noices.

3. Deal with sentence endpoints. Find where the sentence ends.

4. Variability in the speech. Even one person can say the same word differently, each time.

5. Find which meaning is stated when **homophones** are used.

homophone --> same pronouncuation but different meaning

6. Filter fillers like "mm", "err", "hmm".



## Components of ASR

1. Digital representation of input

2. Feature extraction. Identify parts of the input containing speech and transform to acoustic parameters.

3. Acoustic Model: 
   
   - Takes the waveform and breaks to small fragments.
   
   - Predicts most likely phonemes of those fragments.

4. Pronounciation Model: Takes sound and ties them together to make words. 

5. Language Model : Takes the  words and ties them together to make meaningful sentences. 

6. Decoder:  Algorithms to search the hypothesis space efficiently. Combines the predictions of acoustic and language model to predict the most likely sentence.
