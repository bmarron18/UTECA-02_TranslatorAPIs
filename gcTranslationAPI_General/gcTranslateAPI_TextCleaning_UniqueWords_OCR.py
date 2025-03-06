#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:33:46 2025

@author: bmarron
"""

# %%

import os
os.getcwd()

print (os.getcwd())



# %%
'''
Step 1
    USE THIS to remove end of line returns from text file
    End of line returns are coded as, /n
    tr is truncate Linux command
    
        delete all newlines
    $ tr --delete '\n' < yourfile.txt
    
        replace newlines with space
    $ tr '\n' ' ' < input_filename
    
'''

$ tr '\n' ' ' < Test.txt > Test2.txt

# %%


'''
Step 2
    USE THIS for generating a unique word list from texts
    Gives single words for student vocab lists

https://stackoverflow.com/questions/43025188/regular-expression-re-findall-for-set-of-all-alphabetic-words

This will accept words like "don't" and "re-invent" and "cul-de-sac" but will 
reject numbers, underscores, whitespace, quote marks, and other punctuation.

    re.findall(r"[A-Za-z\-\']+", s)
    
The \p{L} matches all Unicode letters regardless of modifiers passed to the regex compile.
    re.findall(r"[p{L}\-\']+", s)
'''
    
import re
from contextlib import chdir

with chdir('/home/bmarron/Desktop'):
    M = []
    with open('Test2.txt') as f:
        for line in f.readlines():
            for word in line.split():
                word = re.findall('[A-Za-zñáéíóúü\,\-\.\)]+', word)    #words in español and w/ comma, dash, period
                if word:
                    M.append(word[0])

    S = list(set(M))
    S = sorted(S, key=str.lower)

    with open("output.txt", "w") as f:
        for i in S:
            f.write(i + "\n")



# %%

"""
Step 3
    Use this to find two-word vocab
    Find next word
"""
    # How to find the next word of a specific word in a txt-file
    # https://stackoverflow.com/questions/70730240/q-how-to-find-the-next-word-of-a-specific-word-in-a-txt-file


from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    with open('Test2.txt','r') as f:
        data = f.read()

    search_word = "tecnologías"
    list_of_words = data.split()
    next_word = list_of_words[list_of_words.index(search_word) + 1]
    prev_word = list_of_words[list_of_words.index(search_word) - 1]

    with open("two-word_terms.txt", "a") as f:
        print(prev_word,"",search_word,"",next_word, file=f)
# %%
# %%

'''
    Get word frequencies
'''

import pandas as pd
#pd.options.display.max_colwidth = None
pd.options.display.max_rows = None
    
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):
    
    words = open("clean_test.txt", "r").read().split()
    ordered = sorted(words)
    with open("output.txt", "a") as f:
        print(pd.Series(ordered).value_counts().sort_values(ascending=True), file=f)

# %%





'''
    TEXT CLEANING
    Use sed and 'tr' to
	+ remove all non-printable ASCII characters (garbage characters== !(octal 11-15 || 40-176)).
	+ remove all punctuation
    + NB. 'tr' uses backslash to denote an octal number.
'''

    # open terminal that has file to be counted
    # remove all punctuation
    # overwrite original
    
$ tr -cd '\11-\15\40-\176' < NAME_of_FILE.txt > clean_test.txt &&
sed 's/[[:punct:]]//g' < clean_test.txt > TMP_00 &&
mv TMP_00 clean_test.txt

# %%

from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    # opening and creating new .txt file 
    with open( 
            "CivilLaw_Terms.txt", 'r') as r, open( 
                'output.txt', 'w') as o: 
      
                    for line in r: 
                        #isspace() function 
                        if not line.isspace(): 
                            o.write(line) 
  
    f = open("output.txt", "r") 
    print("New text file:\n",f.read())


  

# %%


# %%

def count_words(line):
    words = line.split()
    return len(words)

f = open("C:/Users/John Green/Desktop/follows.txt", "r")
text = f.read()
#make a list of the file broken into lines
lines = text.split('\n')
max_words = -1
word = ''
for line in lines:
    length = count_words(line)
    if length > max_words:
        max_words = length
        words = line.split()
f.close()
print(words[0])

# %%


    #Total number of words per line in a text file


def count_words(line):
    words = line.split()
    return len(words)

f = open("/home/bmarron/Desktop/TEST.txt", "r")
text = f.read()
#make a list of the file broken into lines
lines = text.split('\n')
max_words = -1
word = ''
for line in lines:
    length = count_words(line)
    if length > max_words:
        max_words = length
        words = line.split()
f.close()
print(words[0])



# %%



# count the occurrences of number of spaces!?

txt = "Just an example here move along" 
count = 1
for i in txt:
    if i == " ":
       count += 1
print(count)





# %%

"""
USE THIS!!
Find next word
"""
    # How to find the next word of a specific word in a txt-file
    # https://stackoverflow.com/questions/70730240/q-how-to-find-the-next-word-of-a-specific-word-in-a-txt-file


with open('/home/bmarron/Desktop/TEST.txt','r') as f:
    data = f.read()

search_word = "ingeniería"
list_of_words = data.split()
next_word = list_of_words[list_of_words.index(search_word) + 1]



# %%



'''
Optical Character Recognition (OCR)
build an OCR engine in Python
'''

https://builtin.com/data-science/python-ocr



    # Install Tesseract. 
    # Successfully installed pytesseract-0.3.13 in /usr/lib/python3/dist-packages
    #pytesseract in ./.local/lib/python3.10/site-packages (0.3.13)

    # for use in terminal
$ sudo aptitude install tesseract-ocr-all

    # foer use in Python
$ pip3 install tesseract


import pytesseract
from PIL import Image
import pytesseract
import numpy as np

    # clean image OCR
filename = "image_01.png" 
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)



    # image cleaning then OCR
import numpy as np
import cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    filename = 'image_02.png'
    img2 = np.array(Image.open(filename))
    img2 = cv2.normalize(img2, norm_img, 0, 255, cv2.NORM_MINMAX)
    img2 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
    img2 = cv2.GaussianBlur(img2, (1, 1), 0)

    text = pytesseract.image_to_string(img2)
    print(text)

