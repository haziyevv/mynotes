# TERMS

1. **Sampling Frequency**: number of frames per second. 16khz, means 16000 frames per second.

2. **Resolution:** How many bits a frame will take. 16bit is used generally.

3. **Phoneme**: Simplest sound unit. Written representation of  a voice. Example: $\theta$ 

4. **Grapheme:** Representation of phoneme with asci characters. Example: th

5. **Amplitude**: Loudness of the sound

6. **Frequency**: The pitch of the sound

7. **Timbre**: Quality of the sound or the identity of the sound. (Sound difference between a violin and a piano)

8.  











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









## Feature Extraction

1. Some basic tools:

```
import librosa --> main asr feature extraction tool
import librosa.display --> for plots
import noisereduce as nr --> best noice reducer, 
                    uses same method as audacity
```

2. to load the waveform to numpy we will use librosa:

```
waveform, sampling_rate = librosa.load("audio_file.wav")
```

wavefrom --> numpy array

sampling rate is the sampling rate of the audio

```
waveform
array([0.        , 0.        , 0.        , ..., 0.04594884, 0.05876281,
       0.        ], dtype=float32)
```

3. To display the waveform:

```
librosa.display.waveplot(waveform)
```

<img title="" src="figures/waveform.png" alt="">

4. To reduce the noice in the audio:

```
noisy_part = waveform[0:25000]  
reduced_noise = nr.reduce_noise(audio_clip=waveform, 
                                noise_clip=noisy_part, 
                                verbose=False)
```

Now draw the noice reduced audio:

<img title="" src="figures/noice_reduced.png" alt="">

5. Next step is to trim the silences:

```
trimmed, index = librosa.effects.trim(reduced_noise, 
                                      top_db=20, 
                                      frame_length=512, 
                                      hop_length=64)
```

**top_db** --> threshold for decibel. So decibel below than top_db will be trimmed.
