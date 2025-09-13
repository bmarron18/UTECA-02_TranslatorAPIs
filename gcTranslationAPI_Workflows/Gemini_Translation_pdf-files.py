#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:20:22 2025

@author: bmarron / Gemini 2.5 Flash /
Gemini API Coding Guidelines (Python)
https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md

Document understanding (Gemini)
https://ai.google.dev/gemini-api/docs/document-processing

HTML-to-pdf
https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python

"""


# %%

### Translation of mime-type = "application/pdf" files ####

'''
This script will:
1.  Read an English (or any other language) text file.
2.  Construct a clear translator prompt (config) for the 
    Gemini 2.5 Flash model.
3.  Send the config to the Gemini 2.5 Flash model.
4.  Write the Spanish (or any other language) translation to 
    a new file.

Additional info follows the script

'''


# %%


from google import genai
from google.genai import types
from pathlib import Path
import os

# --- Define Files and File Paths ---
    # .txt files already exist on Desktop (make 'em!)
    # Change the languages as needed
    
INPUT_FILE = "english.pdf"  
OUTPUT_FILE = "spanish.html"

doc_to_translate = INPUT_FILE;
doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
input_filepath = os.path.join(doc_dir, doc_to_translate)
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Retrieve the PDF as PosixPath
filepath = Path(input_filepath)

#--- Set the API Key ---
    # Get my Gemini API Key here:
    # /home/bmarron/Desktop/UTECA/GithubToken_UTECALogins.txt

API_KEY = "MY_API_KEY"
client = genai.Client(api_key=API_KEY) 


#--- The Prompt and Select Languages ---
    # Change translation "to" and "from" languages as needed



#--- The API call to the AI ---
prompt = "Translate the following pdf (in English) to natural, \
    fluent Spanish and generate the output in HTML."
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
               system_instruction="You are an expert liguist \
                   specializing in translation. Maintain the original \
                   meaning, tone, and any specific formatting (like line breaks, paragraphs).\
                   Provide ONLY the requested translation without any additional \
                   commentary, introductory phrases, other language translations, \
                   or conversational remarks."),
    contents=[types.Part.from_bytes(
            data=filepath.read_bytes(),
            mime_type='application/pdf'
            ),
            prompt]
    )

#--- Generate output to Python---
#print(response.text)

#   OR

#--- Generate output to ,txt file---
html_text = response.text

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(html_text)
     
print(f"Translation complete! Translated text saved to '{output_filepath}'.")




# %%

### Additional info  ############

'''
----   Explanation of the Gemini Prompt ------------

This is the most critical part for getting good results. 
We are telling Gemini:

**Role-playing:
    "You are an expert linguist..." This helps the model adopt 
    the right persona.

**Clear Task:
    "Translate the following English text into natural, fluent 
    Spanish."

**Key Instructions:
    "Maintain the original meaning, tone, and any specific 
    formatting..." (Crucial for text files).
    
    "Provide ONLY the Spanish translation, without any additional
    commentary..." (Prevents the model from adding things like 
    "Here is your translation:" or "I have translated the text 
    for you.").


'''
# %%
