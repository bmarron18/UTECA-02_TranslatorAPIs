#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:20:22 2025

@author: bmarron / Gemini 2.5 Flash /
Gemini API Coding Guidelines (Python)
https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md

Google search
    types.GenerateContentConfig in the Gemini API 
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
from pathlib import Path
import os

# --- Define Files and File Paths ---
    # create two (2) empty .txt files on the Desktop
        # ==> INPUT_FILE will hold the text To Be Translated
        # ==> OUTPUT_FILE will hold the Translated text from the AI

    # Remove all quotation marks in the INPUT_FILE o/w Gemini will just \
    # translate the text inside the quotes
    # watch file name for uploaded INPUT_FILE 
        # ==> strictly alpha! 
        # ==> NO dashes or underline (won't upload to Gemini)
    
    
    # Change the language names in the files as needed
    
INPUT_FILE = "englishTBT.txt"  
OUTPUT_FILE = "spanish_T.txt"


    # set up the file paths for the input / output files
    # set the file path to your Desktop
    
doc_to_translate = INPUT_FILE
doc_to_print = OUTPUT_FILE
doc_dir = "/home/bmarron/Desktop"
input_filepath = os.path.join(doc_dir, doc_to_translate)
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Retrieve the UNPUT_FILE as PosixPath
filepath = Path(input_filepath)


#--- Set the API Key ---
    # Retrieve your API key from its secret location
    # type in your API key (in quotes)
    # erase API key when finished with translation activities

#API_KEY = "MY_API_KEY"
client = genai.Client(api_key=API_KEY)

'''
#--- Read and process file to be translated (file UPLOADED) ---

uploadedfile = client.files.upload(
    file=input_filepath,
    config=dict(mime_type='text/plain')
    )
'''
#   --- OR ---


#--- Read and process file to be translated (file NOT UPLOADED)---

processedfile = types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='text/plain'
        )


#--- The Prompt and Selected Languages ---
    # Change translation "to" and "from" languages as needed

prompt = "Translate the following English text into natural, fluent Spanish. \
		Maintain all specific formatting (line breaks, indents, spaces, paragraphs)."

#--- The API call to the AI with system (behavior) instructions ---
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are an expert liguist \
            specializing in translation. Maintain the original \
            meaning and tone. Provide ONLY the requested translation without \
            any additional commentary, introductory phrases, other language \
            translations or conversational remarks."),
#    contents=[uploadedfile, prompt]
    contents=[processedfile, prompt]
    )

#--- Output to IPython window ---
#print(response.text)

#   --- OR ---

#--- Output to OUTPUT_FILE---
GeminiOutput = response.text

with open(output_filepath, "w", encoding="Latin-1") as f:
     f.write(GeminiOutput)
     
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
