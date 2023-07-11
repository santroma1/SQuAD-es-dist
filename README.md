# SQuAD-es-dist
__SquAD-es-dist__ is a small scale MCQ dataset based on SQuAD-es with distractors included from the same text. 

__SQuAD-es-dist__ contains texts from the dataset SQuAD-es that can be found in the [Translate-Align-Retrieve](https://github.com/ccasimiro88/TranslateAlignRetrieve) repository.

A question, correct answer and distractors were then manually tagged for 980 questions using the [Textinator](https://github.com/dkalpakchi/Textinator) tool.

This repository has the data split in training, development and test set, in approximate splits of 85%, 10%, and 5%, respectively.

|                        | training           | dev                | test            |
|:-----------------------|:-------------------|:-------------------|:----------------|
| # of texts             | 810                | 95                 | 48              |
| # of MCQs              | 835                | 95                 | 50              |
| # of D                 | 3.16 +- 0.74       | 3.23 +- 0.69       | 3.20 +- 0.75    |
| Len(Text)              | 158.21 +- 54.86    | 158.45 +- 49.53    | 158.18 +- 60.75 |
| Max(Text)              | 453.0              | 297.0              | 449.0           |
| Len(A)                 | 4.36 +- 4.49       | 5.45 +- 4.70       | 4.76 +- 4.37    |
| Max(A)                 | 26.0               | 22.0               | 19.0            |
| Len(D)                 | 4.59 +- 4.97       | 5.62 +- 5.53       | 4.08 +- 3.46    |
| Max(D)                 | 43                 | 32                 | 17              |
| \|Len(A) - Len(D)\|      | 1.69 +- 2.28       | 2.08 +- 2.52       | 1.85 +- 2.00    |
| Max(\|Len(A) - Len(D)\|) | 16.666666666666668 | 10.333333333333334 | 8.0             |

The respository also contains a ChatGPT prompt that was used to aid the tagger in the task of tagging. The results from ChatGPT were far from perfect, but served as a great starting point to find a plausible question, correct answer and distractors. 

The data was used to fine-tune a BERT model for distractor generations. Details can be found in the [SweQUAD-MC](https://github.com/dkalpakchi/SweQUAD-MC) respository to fine-tune a BERT model for distractor generations. The Spanish BERT used for distractor generation __SQuAD-es-dist__ was [BETO](https://github.com/dccuchile/beto).

Lastly a script is included that uses GPT-3 in a zero-shot fashion to produce distractors in the test set. 