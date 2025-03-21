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
=========  Extraction of Vocab  ==============================
'''
# %%
'''
Step 1
    USE THIS to remove end of line returns from text file
    End of line returns are coded as, /n
    tr is truncate Linux command
'''
    
        # delete all newlines
    $ tr --delete '\n' < yourfile.txt
    
        # replace newlines with space
    $ tr '\n' ' ' < input_filename
    

    # USE THIS!! Step 1
$ tr '\n' ' ' < VocabDump.txt > Test2.txt

# %%


'''
Step 2
    *Generating a unique word list from texts
    *Gives single words for student vocab lists
'''

https://stackoverflow.com/questions/43025188/regular-expression-re-findall-for-set-of-all-alphabetic-words

This will accept words like "don't" and "re-invent" and "cul-de-sac" but will 
reject numbers, underscores, whitespace, quote marks, and other punctuation.

    re.findall(r"[A-Za-z\-\']+", s)
    
The \p{L} matches all Unicode letters regardless of modifiers passed to the regex compile.
    re.findall(r"[p{L}\-\']+", s)

https://docs.python.org/3/library/re.html
In regex, there are 12 characters with special meanings: 
    the backslash \, 
    the caret ^, 
    the dollar sign $, 
    the period or dot ., 
    the vertical bar or pipe symbol |, 
    the question mark ?, 
    the asterisk or star *, 
    the plus sign +, 
    the opening parenthesis (, 
    the closing parenthesis ), 
    the opening square bracket [, and 
    the opening curly brace {, 
These special characters are often called metacharacters and should be escaped with backslash Ab\(123\) if used as literal.
This can be automagically achieved using re.escape()

# %%
 


    # USE THIS!!   Step 2
import re
from contextlib import chdir

with chdir('/home/bmarron/Desktop'):
    M = []
    with open('Test2.txt') as f:
        for line in f.readlines():
            for word in line.split():
                word = re.findall('[A-Za-zñáéíóúüÁÉÍÓÚ\,\-\.\“\\(]+', word)    #words in español and w/ comma, dash, period
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

# %%


    # USE THIS!! Step 3 NB ==> Replace search_word
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    with open('Test2.txt','r') as f:
        data = f.read()

    search_word = "Zipf"
    list_of_words = data.split()
    next_word = list_of_words[list_of_words.index(search_word) + 1]
    prev_word = list_of_words[list_of_words.index(search_word) - 1]

    with open("two-word_terms.txt", "a") as f:
        print(prev_word,"",search_word,"",next_word, file=f)

# %%

=========== pdf Manipulations ========================

# %%

"""
pypdf module
"""
https://pypdf.readthedocs.io/en/stable/user/installation.html
https://pypdf.readthedocs.io/en/stable/user/adding-pdf-annotations.html

Hence I would distinguish three types of PDF documents:

    #Digitally-born PDF files: The file was created digitally on the computer. It can contain images, texts, links, outline items (a.k.a., bookmarks), JavaScript, … If you Zoom in a lot, the text still looks sharp.

    #Scanned PDF files: Any number of pages was scanned. The images were then stored in a PDF file. Hence the file is just a container for those images. You cannot copy the text, you don’t have links, outline items, JavaScript.

    #OCRed PDF files: The scanner ran OCR software and put the recognized text in the background of the image. Hence you can copy the text, but it still looks like a scan. If you zoom in enough, you can recognize pixels.

# %%


$ cd ~ 
pip install pypdf[full]

# Spyder py modules here
/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages

# move pypdf and Pillow
$ cd ~/.local/lib/python3.10/site-packages
mv -R pypd* ~/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/


$ cd /usr/lib/python3/dist-packages
$ sudo mv Pillo* ~/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/


# %%

"""
Add text box comment
font color hex codes
"""

import os
import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText


# path to the document
doc_to_comment = "terminologia 6.1_Leslie.pdf" ;
doc_dir = "/home/bmarron/Desktop" ;
pdf_path = os.path.join(doc_dir, doc_to_comment)


# Fill the writer with the pages you want
reader = PdfReader(pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Create the annotation and add it
annotation = FreeText(
    text="LATE\n \n 8.0",
    rect=(200, 700, 150, 650), # a square! why???
    #font="New Times Roman",
    #bold=True,
    #italic=True,
    #font_size="20pt",
    #font_color="000000",
    border_color="d70029",
    background_color="ffffff",
)

# Set annotation flags to 4 for printable annotations.
# See "AnnotationFlag" for other options, e.g. hidden etc.
annotation.flags = 4

writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("/home/bmarron/Desktop/annotated.pdf", "wb") as fp:
    writer.write(fp)
    
    
# %%

========== Optical Character Reader for Scanned pdf Files ===============


# %%
'''    OCR for optical pdf files
        *create text files for Extraction of Vocab
'''
    # STEP 1 ==> pdf to png
    # if a multipage pdf, will out individual ,pngs; one per pdf page
$ pdftoppm -png Webdoc.pdf Webdoc

    # STEP 2a ==> one png file to txt 
$ tesseract Webdoc-1.png Webdoc-1 --dpi 250^C

    # STEP 2b ==> multiple ,png
    # loop thru Webdoc-xx.png files
    # create a text file from each image
$ for i in Webdoc-??.png; 
do tesseract "$i" "text-$i" -l eng; 
done

    # STEP 3 ==> compile/concatentae text files (if needed)
$ cat text-Webdoc* > complete.txt

# %%
'''
    Merge pdf files into one
'''


$ pdfunite in-1.pdf in-2.pdf in-n.pdf ouput.pdf

$ pdfunite W*01.pdf W*02.pdf W*03.pdf W*04.pdf W*05.pdf W*06.pdf W*07.pdf W*08.pdf W*09.pdf W*10.pdf W*11.pdf W*12.pdf ouput.pdf



# %%


# %%
'''
Optical Character Recognition (OCR)
'''

https://builtin.com/data-science/python-ocr



    # Install Tesseract in Linux and Python
    # Successfully installed pytesseract-0.3.13 in /usr/lib/python3/dist-packages
    # pytesseract in ./.local/lib/python3.10/site-packages (0.3.13)

    # for use in terminal
$ sudo aptitude install tesseract-ocr-all

    # for use in Python
$ pip3 install tesseract


# %%

'''
Tesseract   ==> image files only
            ==> unable to read PDFs. rom a PDF, you can 
            ===> use another utility first to generate a set of images
            ==> A single image will represent a single page of the PDF
            ==> pdftppm utility
'''

https://www.howtogeek.com/682389/how-to-do-ocr-from-the-linux-command-line-using-tesseract/

-r number
Specifies the X and Y resolution, in DPI.  The default is 150 DPI.


    # pdf to images is turing-01.png" "turing-02.png" etc
$  pdftoppm -png Web.pdf Web

    # JPEG option
    <opt>=<val>[,<opt>=<val>]"
-jpegopt 
$ pdftoppm -jpegopt=90[,-jpegopt=n] PDF-file PPM-root


    # general tesseract
    # creates "recital.txt" at 150 dpi
$ tesseract recital-63.png recital --dpi 150


    # loop thru turing-xx.png files
    # create a text file from each image
$ for i in turing-??.png; do tesseract "$i" "text-$i" -l eng; done;

    # concatenate text files into one file
$ cat text-turing* > complete.txt




# %%

'''
build an OCR engine in Python
'''

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


# %%

'''
=========  Misc Text Options =======================
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



