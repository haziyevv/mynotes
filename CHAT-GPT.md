1. InstructGPT is the sibling model of chatgpt
2. Reinforcement Learning From human Feedback
3. Process:
    1. Open AI-a input olunmus propmtlarin, outputunu el ile yaradirlar.
    2. Human Labeled comparisons between outputs from their models on a large api prompts-
        1. Then they train a reward model from this dataset, to predict which model output their labelers will prefer
        2. Then they use this RM as a reward function and fine tune their supervised learning baseline to maximize reward using PPO algorithm.

        
        
        

## TransferTransfo
1. GPT2 language model is used. This language model is trained with a single input: a sequence of words.
2. But in a dialog setting, the model have to use several types of contexts to generate an output sequence:
    1. one or several persona sentences,
    2. the history of the dialog with at least the last utterance from the user,
    3. the tokens of the output sequence that have already been generated since we generate the output sequence word by word.



## End-to-End Neural Pipeline for Goal-Oriented Dialogue Systems using GPT-2

#### Multiwoz dataset
This is a large scale fully annotated corpus, where human, which is a tourist is talking to the system across multiple domains.

Belief state has three sections, semi, book and booked. Semi refers to the slots for a particular domain. 




question: What is BLEU score? 
answer: metric used to evaluate generated text. Divide the number of correctly predicted tokens to the number of tokens in the generated text. To make this more robust. Only get the number of tokens in numerator as much as they exist in the reference text. For example: reference - **the cat sat on the mat**. generated- **the the the**. **score = 2/3**. Numerator is 2 not 3 as the exists only 2 times in the reference. Also to make more robust, multiply this score with brewity score, to punish generated text if it is too small. BR = min(1, **e^(1-l_ref/l_gen)**. now calcuate the score again. BR= min(1, e^(1-6/3)) = 1/8. Score = 2/3 * 1/8.







## **COLLOSAL AI**

- Efficient training system for general large AI models
- Completely open sources and requires only minimal modifications to train existing DL projects
- Also with parallelism, we can deploy existing projects to large scale computing clusters. 
- The Gemini mechanism designed by Colossal-AI, **efficiently manages and utilizes the heterogeneous memory of GPU and CPU**, so that tensors are dynamically distributed in the storage space of CPU-GPU during the training process, therefore model training can break the GPU’s memory barrier.
- Divide the training into two stages: warmup stage and non-warmup stage. In the initial warmup phase, memory information is monitored; in the non-warmup phase, the collected information is used to efficiently move tensors to minimize CPU-GPU data movement.
- Colossal-AI obtains the usage of CPU and GPU memory by sampling in the warmup stage
- While the usage of non-model data can be obtained by comparing the maximum system memory usage and model memory usage between two moments. 
- The memory usage of the model could be known by querying the memory manager
- All tensors from models are managed by the memory manager, and each tensor is marked with information of states, including HOLD, COMPUTE, FREE, etc.



### Colossal-AI: A Unified Deep Learning System for large-scale parallel training

- A unified interface to scale your sequential code of model training to distributed environments
- Compared to baseline system, can achieve up to 2.76 times training speedup on large-scale models
- Since adaptive optimizers are applied in giant model training, memory consumption comes from model parameters, layer activations, gradients and optimizer states.
- They refer to **model parameter, gradients and optimizer states** as **model data** and **layer activations** as **non-model data**.
- 10 billion parameters in **Float 16** (2 byte) format can already cosume 20 gb of model memory.
- **Data Parallelism** is the most popular parallelism method supported by deep learning methods. But this method requires holding the full model on a single device. 
- **Megatron LM** was proposed to train Transformer based models by utilizing optimized pipeline and tensor parallelism. 

#### Heterogenous Training

- DeepSpeed proposed zero-offload which moves the tensors from GPU to CPU of NVME disks when not in use to make room for larger models. 







## Convlab: Multi-Domain End-to-End Dialog System Platform

- An open-source multi-domain end-to-end dialog system platform
- Consists of a rich set of modelling tools and runtime engines for building task-oriented bots of different types and an end-to-end evaluation platform.
- There are two architectures of dialog systems:
  - Modular architecture: consists of NLU, DST (dialog state tracker), POL (dialog policy) and NLG
  - Fully end to end architecture: 
- For **MultiWOZ** dataset offers reference models rangin from individual components to end to end models.



## ConvLab-2: An Open-Source Toolkit for Building, Evaluating, and Diagnosing Dialogue Systems

- On top of ConvLab1, they have developed an analysis tool and and interactive tool
  - **analysis tool** shows statistics and common mistakes from dialogues
  - **interactive tool** provides a user interface to diagnose dialogue system by interacting with the system and modifying the output of each system component.



## ConvLab-3: A Flexible Dialogue System Toolkit Based on a Unified Data Format

- The diversity in data formats and ontologies between datasets brings inconvenience to model adaptation and uniform evaluation, which potentially hinders the study of model generalization and knowledge transfer across datasets. To address this issue, we define a unified data format that serves as the adapter between TOD (task oriented dialog) datasets and models
- Datasets are first transformed to unified dataset format and then fed into the models
- Enhances the utility of reinforcement learning for dialog policies
- 

### Unified Data Format

- A unified dataset in ConvLab-3 consists of **dialogues**, **ontology**, and **database** 

- Once a dataset is transformed into the unified format, it can be immediately used by models on the tasks it supports. 

- Similarly, a model supporting the unified format can access all transformed datasets.

- In our unified data format, a dataset consists of (1) an ontology that defines the annotation schema, (2) dialogues with transformed annotations, and (3) a database or API interface that links to external knowledge sources.

- {'Context': "I would like a taxi from Saint John's college to Pizza Hut Fen Ditton. EOS What time do you want to leave and what time do you want to arrive by? EOS I want to leave after 17:15. EOS Booking completed! your taxi will be blue honda Contact number is 07218068540 EOS Thank you for all the help! I appreciate it.", 

- 'Knowledge': 'taxi leave at is 17:15 ; destination is pizza hut fenditton ; departure is saint johns college', 'Response': 'Agent: You are welcome.  Is there anything else I can help you with today?', 'Dataset': 'multiwoz21'}

- ```python
  _input = ' EOS '.join(context.split(' EOS ')[-10:])
  _response = 'Belief: ' + kb + response
  ```

- 





# Adding External Knowledge and Controllability to Language Models with Megatron-CNTRL

- In this work, we try to address this by making our large language models both controllable and consistent with an external knowledge base.
- Generation Process:
  - Given the story context, a keyword predictor model first predicts a set of keywords for the next sentence yet to be generated.
  - A knowledge retriever then takes the generated keywords and queries an external knowledge base where each knowledge triple is converted into natural language “knowledge sentences” using templates.
  - A contextual knowledge ranker then ranks the external knowledge sentences based on their relevance to the story context.
  - Finally, a generator takes the story context, as well as the top-ranked knowledge sentences as input, and generates the next sentence in the story. The output sentence is appended to the story context and steps 1-4 are repeated.
- Keyword generation is modeled as a seq2seq model, which takes story as input and ouputs a set of keywords. Megatron model is used for keyword generation. 
- 





## Large Scale Multi-Actor Generative Dialog Modeling

- Generative Conversation Control model, an augmented and fine-tuned GPT-2 model, that conditions on past reference conversations.
- They introduce a data collection procedure to obtain 10.3M conversations from reddit. 

## Extensible Prompts for Language Models

- XPrompt is used for prompting a large language model beyond natural language (NL)
- Compared with NL (natural language) prompts, X-Prompt additionally introduces a vocabulary of imaginary words.

## In-Context Retrieval-Augmented Language Models

- **RALM** (incontext retrieval augmented language modeling.) employs a zero-effort document integration mechanism by simply  prepending the selected documents to the LM's input text
-  In-Context RALM is simply about finding documents relevant to the LM generation, and prepending them as input to the LM, without further changing its operation.
- Retrieval augmented language models (RALMs) add an operation that retrieves one or more documents from an external corpus C, and condition the above LM predictions on these documents.

## A Survey for In-context Learning

-  In-context learning is a paradigm that allows language models to learn tasks given only a few examples in the form of demonstration. 
  - Essentially, it estimates the likelihood of the potential answer conditioned on the demonstration by using a well-trained language model.

## MetaICL: Learning to Learn In Context

- This metatraining enables the model to more effectively learn a new task in context at test time, by simply conditioning on a few training examples with no parameter updates or task-specific templates
- we show that MetaICL is complementary to human-written instructions, and the best performance can be achieved by combining both approaches.
- MetaICL tunes a pretrained language model on a large set of tasks to learn how to incontext learn, and is evaluated on strictly new unseen tasks.







## LAD: Language Models as Data for Zero-Shot Dialog

- The goal of this work is to create synthetic data that is sufficient to train a sample-efficient and robust model.
- For intent prediction, we define the schema to be a single utterance u for each intent i ∈ I. Slot filling similarly relies on one utterance u for each slot type s ∈ S. H
- Next action prediction has three constraints. The first two constraints are equivalent to those of intent prediction and slot filling. As such, the schema includes both (1) one utterance for each intent and (2) a set of slot values for each slot type





## Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- That is, instead of finetuning a separate language model checkpoint for each new task, one can simply “prompt” the model with a few input–output exemplars demonstrating the task.
- 

