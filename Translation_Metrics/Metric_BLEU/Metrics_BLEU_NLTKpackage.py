#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:35:19 2025

@author: bmarron
"""

# %%

'''
The BLEU (Bilingual Evaluation Understudy) Metric 
using the Natural Language Tool Kit (ntlk) in Python

'''




# %%
'''
BLEU Score: Test Run
'''

from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import sent_tokenize, word_tokenize


    # Define reference texts 
 
reference_text_1 = "The quick brown fox jumps over the lazy dog. \
    And finds himself caught." 
reference_text_2 = "A fast brown fox leaps over a lazy dog. \
    And is captured."

candidate_text =  "The quick brown fox hops over the slow-moving dog. \
    And gets caught."


   # list sentences and then tokenize to words
sentences = [reference_text_1, reference_text_2]


references = [word_tokenize(sentence, "english") for sentence in sentences]
candidate = word_tokenize(candidate_text, "english")

weights=(.50, 0.50, 0, 0)


bleu_score = sentence_bleu(references, candidate, weights)

 
print(bleu_score)


# %%

'''
METEOR Score
'''
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.translate.meteor_score import single_meteor_score 

# Define candidate and reference sentences 
reference_text= "The quick brown fox jumps over the lazy dog. And finds himself caught." 
candidate_text = "A fast brown fox leaps over a lazy dog. And is captured."


ref = word_tokenize(reference_text)
hypo = word_tokenize(candidate_text)


# Calculate METEOR score 
score = single_meteor_score(ref, hypo) 

# Print the result 
print(f"METEOR Score: {score:.3f}")

# %%
'''
Tokenizing

'''

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = "NLTK is a powerful library for natural language processing. It's widely used! You can do a lot with it."
sentences = sent_tokenize(text)
sent_strg = "".join(sentences)
words = word_tokenize(sent_strg)

print(sentences)

print(words)

# %%


