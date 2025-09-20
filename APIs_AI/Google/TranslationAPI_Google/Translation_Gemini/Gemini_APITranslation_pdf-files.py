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

### Natural Language Translation of .pdf-to-(other-file-types) ####

'''
This script will:
1.  Read an English (or any other language) pdf file.
2.  Construct a clear translator request (prompt + config) for the 
    Gemini 2.5 Flash model.
3.  Send the request to the Gemini 2.5 Flash model.
4.  Write the Spanish (or any other language) translation to 
    a new file type.

Document types available for Gemini output:
    text/plain
    text/html
    text/json
    text/x-tex
    
Additional info follows the script

'''


# %%


from google import genai
from google.genai import types
from pathlib import Path
import os

# --- Define Files and File Paths ---
    # Create one (1) empty file on the Desktop
        # ==> OUTPUT_FILE will hold the Translated text from the AI
        # ==> file extension should match prompt (eg, ,txt, .tex, docx. etc)
    # Select .pdf file to be translated and place in Desktop
        # ==> INPUT_FILE will hold the .pdf To Be Translated

    # watch file name for INPUT_FILE
        # ==> strictly alpha! 
        # ==> NO dashes or underline (won't upload to Gemini)
    
    # Change the language names in the files as needed
    # Change the file extension of OUTPUT_FILE as needed
    
INPUT_FILE = "englishTBT.pdf"  
OUTPUT_FILE = "spanish_T.tex"


    # set up the file paths for the input / output files
    # set the file path to your Desktop
    
doc_to_translate = INPUT_FILE;
doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
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

#--- Read and process file to be translated (file NOT UPLOADED)---

processedfile = types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf'
        )


#--- The Prompt and Select Languages ---
    # Change translation "to" and "from" languages as needed
    # Change the doc types as needed

prompt = "Translate the following pdf file (in English) to natural, \
    fluent Spanish and generate the output in Latex. That is, the\
    output translation should be formated as a .tex file ready to open Latex."


#--- The API call to the AI ---
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    config = types.GenerateContentConfig(
               system_instruction="You are an expert liguist \
                   specializing in translation. Maintain the original \
                   meaning, tone, and any specific formatting (like line breaks, paragraphs).\
                   Provide ONLY the requested translation without any additional \
                   commentary, introductory phrases, other language translations, \
                   or conversational remarks."),
    contents = [processedfile, prompt]
    )

#--- output to IPython window ---
#print(response.text)

#   OR

#--- Output to OUTPUT_FILE ---
GeminiOutput = response.text

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(GeminiOutput)
     
print(f"Translation complete! Translated text saved to '{output_filepath}'.")




# %%

### Additional info  ############

'''

--- Doc MIME Types ---------------
The most comprehensive list of MIME types is maintained by the 
Internet Assigned Numbers Authority (IANA). 


Text:
    text/plain: Plain text files (.txt) 
    text/csv: Comma-separated values files (.csv) 
    text/html: HyperText Markup Language files (.html, .htm)
    text/x-tex: Various common LaTex files (.tex, .cls, .sty)

Image:
    image/jpeg: JPEG image files (.jpeg, .jpg) 
    image/png: Portable Network Graphics files (.png) 
    image/gif: Graphics Interchange Format files (.gif) 
    image/svg+xml: Scalable Vector Graphics files (.svg) 

Audio:
    audio/mpeg: MPEG audio files (.mp3) 

Video:
    video/mp4: MP4 video files (.mp4) 
    video/webm: WebM video files (.webm) 

Application:
    application/pdf: Portable Document Format files (.pdf) 
    application/json: JavaScript Object Notation files (.json) 
    application/zip: ZIP compressed archive files (.zip) 
    application/octet-stream: A general-purpose type for unspecified binary data 
1*    application/vnd.openxmlformats-officedocument.wordprocessingml.document (.docx)


1* Gemini gave me a .json file when this mime type was requested

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
