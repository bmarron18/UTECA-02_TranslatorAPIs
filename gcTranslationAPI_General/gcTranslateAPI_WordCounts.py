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
Use 'tr' to
	+ remove all non-printable ASCII characters (garbage characters== !(octal 11-15 || 40-176)).
	+ NB. 'tr' uses backslash to denote an octal number.
'''

$ tr -cd '\11-\15\40-\176' < test.txt > clean_test.txt

   

     # option to overwrite original
$ tr -cd '\11-\15\40-\176' < test.txt > clean_test.txt \
&& mv clean_test.txt test.txt




# %%

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

