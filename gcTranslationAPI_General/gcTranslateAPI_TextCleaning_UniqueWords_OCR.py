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


# %%

'''
    USE THIS for student word lists !!
'''
    
import re
from contextlib import chdir

with chdir('/home/bmarron/Desktop'):
    M = []
    with open('EXCERPTS_P3_EPA_Guidance-for-SOPs.txt') as f:
        for line in f.readlines():
            for word in line.split():
                word = re.findall('[A-Za-z]+', word)
                if word:
                    M.append(word[0])

    S = list(set(M))
    S = sorted(S, key=str.lower)

    with open("output.txt", "w") as f:
        for i in S:
            f.write(i + "\n")
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

