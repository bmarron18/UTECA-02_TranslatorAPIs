#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:35:19 2025

@author: bmarron
"""

# %%

'''
Using the Natural Language Tool Kit (ntlk)
[see installation in 'Install-Info_NLTK-package.txt']

'''

# %%

import nltk
nltk.download()

# %%

'''
Test Code

'''

from nltk.translate.bleu_score import sentence_bleu

# Define your desired weights (example: higher weight for bi-grams)
weights = (0.25, 0.25, 0, 0)  # Weights for uni-gram, bi-gram, tri-gram, and 4-gram

# Reference and predicted texts (same as before)
reference = [["the", "picture", "is", "clicked", "by", "me"],
             ["this", "picture", "was", "clicked", "by", "me"]]
predictions = ["the", "picture", "the", "picture", "by", "me"]

# Calculate BLEU score with weights
score = sentence_bleu(reference, predictions, weights=weights)
print(score)

# %%

#from nltk.translate.bleu_score import corpus_bleu

from nltk.tokenize import sent_tokenize

text = "NLTK is a great NLP toolkit. It makes processing text easy!"
sentences = sent_tokenize(text)
print(sentences)

# %%

import os
from nltk.tokenize import sent_tokenize, word_tokenize

    # Setup for output
OUTPUT_FILE = "tokenized_refs.txt"

doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Define reference texts
    # tokenize to sentences and then to words
reference_text_1 = "This is a long and complex reference text for evaluating the machine translation output. It contains multiple sentences and aims to provide a comprehensive example."
reference_text_2 = "Another reference text that is also long and provides a different perspective on the same topic. This helps in capturing more nuances."

references = [
        [word_tokenize(sent) for sent in reference_text_1.split('. ') if sent],
        [word_tokenize(sent) for sent in reference_text_2.split('. ') if sent]
    ]

    # If the list contains elements of other data types 
    # you need to convert them to strings before joining
    # use map(str, <list_name>)
refs_string = ",".join(map(str, references))

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(refs_string)

#print(references)

# %%
'''
BLEU Score
'''

import os
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
from nltk.tokenize import sent_tokenize, word_tokenize

    # Setup for output
OUTPUT_FILE = "tokenized_refs.txt"

doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Define reference texts 
 
reference_text_1 = "I think therefore I am."
#reference_text_2 = "Another reference text that is also long and provides a different perspective on the same topic. This helps in capturing more nuances."

candidate_text = "I think therefore I am."
   # split sentences and then tokenize to words
#references = [
#        [word_tokenize(sent) for sent in reference_text_1.split('. ') if sent],
#        [word_tokenize(sent) for sent in reference_text_2.split('. ') if sent]
#    ]

references = [word_tokenize(sent) for sent in reference_text_1.split('. ') if sent]
candidate = [word_tokenize(sent) for sent in candidate_text.split('. ') if sent]

ref_sents = sent_tokenize(reference_text_1)
ref_sents_strg = "".join(ref_sents)
ref_words = word_tokenize(ref_sents_strg)


cand_sents = sent_tokenize(candidate_text)
cand_sents_strg = "".join(cand_sents)
cand_words = word_tokenize(cand_sents_strg)


weights=(.50, 0.50, 0, 0)

bleu_score = sentence_bleu(ref_words, cand_words, weights)
#bleu_score = corpus_bleu(references, candidate, weights)
#bleu_score = corpus_bleu(ref_words, cand_words, weights)
 
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


