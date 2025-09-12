#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:20:22 2025

@author: bmarron / Gemini 2.5 Flash /
Gemini API Coding Guidelines (Python)
https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md


"""


# %%

### Translation of mime-type = "text/plain" files ####

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
import os

# --- Define Files and File Paths ---
    # .txt files already exist on Desktop (make 'em!)
    # Change the languages as needed
    
INPUT_FILE = "english_text.txt"  
OUTPUT_FILE = "spanish_text.txt"

doc_to_translate = INPUT_FILE;
doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
input_filepath = os.path.join(doc_dir, doc_to_translate)
output_filepath = os.path.join(doc_dir, doc_to_print)


#--- Set the API Key ---
    # Get my Gemini API Key here:
    # /home/bmarron/Desktop/UTECA/GithubToken_UTECALogins.txt
    
API_KEY = "MY_KEY_ALPHANUMERIC"
client = genai.Client(api_key=API_KEY)

#--- upload file to be translated ---
    # watch file name for uploaded file ==> strictly alpha! 
    # NO dashes or underline (won't upload)
    
uploadedfile = client.files.upload(
        file=input_filepath,
#       config=dict(mime_type='application/pdf')
       config=dict(mime_type='text/plain')
    )

#--- The Prompt and Select Languages ---
    # Change translation "to" and "from" languages as needed

role = types.GenerateContentConfig(
    system_instruction="You are an expert linguist specializing in translation.\
           Translate the following English text into natural, fluent Spanish.\
           Maintain the original meaning, tone, and any specific formatting (like line breaks, paragraphs).\
           Provide ONLY the Spanish translation without any additional commentary, introductory phrases, or conversational remarks.",
)

#--- The API call to the AI ---
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=role,
    contents=[uploadedfile],
    )

#--- Generate output to Python---
#print(response.text)

#   OR

#--- Generate output to ,txt file---
translated_text = response.text

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(translated_text)
     
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
