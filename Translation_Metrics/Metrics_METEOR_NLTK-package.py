#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:35:19 2025

@author: bmarron
"""

# %%

'''
METEOR Metric using the Natural Language Tool Kit (ntlk)

'''


# %%

'''
METEOR Score: Test Run
'''
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score 

# Define candidate and reference sentences 
reference_text= "The quick brown fox jumps over the lazy dog. \
    And finds himself caught." 
candidate_text = "A fast brown fox leaps over a lazy dog. \
    And is captured."


ref = word_tokenize(reference_text, "english")
hypo = word_tokenize(candidate_text, "english")


# Calculate METEOR score 
score = single_meteor_score(ref, hypo) 

# Print the result 
print(f"METEOR Score: {score:.4f}")

# %%


