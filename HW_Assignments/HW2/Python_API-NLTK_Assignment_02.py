#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:38:36 2025
Updted 20 Oct 2025

@author: bmarron18
"""

# %%

======== HW Assignemts: Assignment 2 ======================

# %%

#######################################
Translation with Google Gemini 2.5 Flash
########################################

# %%
'''
Step 1:
Translation Fourth Section Preamble from "Joy Luck Club" with Google Gemini 
'''

from google import genai
from google.genai import types
from pathlib import Path
import os


#--- API Key ---------------------
    # API_KEY is saved as an ENV VARIABLE on home compu
    # (See "Info_Gemini_API.txt for procedure)

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)


    # API_KEY also can be inserted directly
#client = genai.Client(api_key=ACTUAL_API_KEY)




# --- Prep Files, and Define Files and File Paths -------
    # INPUT_FILE
        #==> this is the .txt file (T)o (B)e (T)ranslated
        #==> ADD quotation marks to the begiining and end of the INPUT_FILE 
        #==> Move .txt file (T)o (B)e (T)ranslated to the Desktop
 
   # OUTPUT_FILE 
       #==> will hold the (T)ranslated text from the AI
       #==> this file will be generated automatically by Python after \
       # the translation is complete
   
    
    # Name the INPUT_FILE and OUTPUT_FILE
    # Change names of files as needed
        # ==> INPUT_FILE must stay as .txt
        # ==> OUTPUT_FILE can be any of the Document types available for \
        # Gemini output (see header of this script)
    
INPUT_FILE = "Gemini_Doc-English_TBT.txt"  
OUTPUT_FILE = "Gemini_Doc-Spanish_T.txt"


    # Set up the file paths for the INPUT_FILE and the OUTPUT_FILE
    # Set the file path to your Desktop
    # Path() represents file+directory paths in a platform-independent manner.
    
doc_to_translate = INPUT_FILE
doc_to_print = OUTPUT_FILE
doc_dir = "/home/bmarron18/Desktop"   #<== OLD HP


    # create paths to files
    # Retrieve files as PosixPaths

input_filepath = os.path.join(doc_dir, doc_to_translate)
input_f = Path(input_filepath)

output_filepath = os.path.join(doc_dir, doc_to_print)
output_f = Path(output_filepath)



#--- Read and process file to be translated ---
    # File UPLOADED to Google
    # (NOT recommended)
'''
uploadedfile = client.files.upload(
    file=input_f,
    config=dict(mime_type='text/plain')
    )
'''

    # File NOT UPLOADED to Google
    # (Recommended)
processedfile = types.Part.from_bytes(
        data=input_f.read_bytes(),
        mime_type='text/plain'
        )



#--- The API call to the AI
    # ==> modify "prompt" (user level) as needed
    # ==> modify "system instruction" (behavior)as needed
    

prompt = "Translate the following English text into standard, natural, \
        and fluent Spanish. Maintain all specific formatting (line breaks, \
        indents, spaces, paragraphs).Do not translate any Chinese characters \
        and leave Chinese pinyin as is."


response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are an expert linguist \
            specializing in translation. Maintain the original \
            meaning and tone. Provide ONLY the requested translation without \
            any additional commentary, introductory phrases, other language \
            translations or conversational remarks."),

    # Select upload or process in-place         
#    contents=[uploadedfile, prompt]    #<== upload file
    contents=[processedfile, prompt]    #<== process in place
    )



#--- Output from AI (response.text) ---

   # Send output to IPython window
#print(response.text)



    # Send output to OUTPUT_FILE
GeminiOutput = response.text

    # Options for encoding: "utf-8" OR "latin-1"
with open(output_f, "w", encoding="utf-8") as f:
#with open(output_f, "w", encoding="latin-1") as f:
     f.write(GeminiOutput)
     
print(f"Translation complete! Translated text saved to '{output_f}'.")

# %%

#######################################
METEOR Score from NLTK
########################################



# %%

'''
Step 2:
METEOR Score fron NLTK
'''

from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score


 
   # Define a reference text created by a human translator
   # The quotes define a "string" in Python
   # If the excerpt has quotation marks, enclose the entire excerpt in single quotes 
   # '"excerpt wirth quotation marks" enclosed in single quotes'
reference_text= '"¡Oh! Hwai dungsyi" —"Pequeña cosita mala"— dijo la mujer, bromeando \
    con su nieta. "¿Te está enseñando Buda a reír sin motivo?" Mientras la bebé seguía \
     borbotando, la mujer sintió un profundo deseo agitarse en su corazón. "Aunque \
    pudiera vivir para siempre," le dijo a la bebé, "todavía no sé de qué manera te \
    enseñaría. Yo fui una vez tan libre e inocente. Yo también me reía sin motivo. \
    Pero más tarde, tiré por la borda mi tonta inocencia para protegerme. Y luego le \
    enseñé a mi hija, tu madre, a deshacerse de su inocencia para que ella tampoco \
    sufriera daño. Hwai dungsyi, ¿estuvo mal este tipo de pensamiento? Si ahora \
    reconozco el mal en otras personas, ¿no es porque yo también me he vuelto malvada? \
    Si veo que alguien tiene una nariz sospechosa, ¿no he olido yo las mismas cosas \
    malas?" La bebé se rió, escuchando los lamentos de su abuela. "¡Oh! ¡Oh! ¿Dices \
    que te ríes porque ya has vivido para siempre, una y otra vez? ¡Dices que eres \
    Syi Wang Mu, la Reina Madre de los Cielos Occidentales, que has vuelto ahora para \
    darme la respuesta! Bien, bien, te escucho.... Gracias, Pequeña Reina. Entonces \
    debes enseñarle a mi hija esta misma lección. Cómo perder la inocencia, pero no \
    la esperanza. Cómo reír para siempre."'
    # Define the candidate text created by an AI translator
    # The quotes define a "string" in Python
candidate_text = '"¡Oh! Hwai dungsyi" —"Pequeña cosita mala"— dijo la mujer, bromeando \
    con su nieta. "¿Te está enseñando Buda a reír sin motivo?" Mientras la bebé seguía \
    balbuceando, la mujer sintió un profundo deseo agitarse en su corazón. "Aunque \
    pudiera vivir para siempre," le dijo a la bebé, "todavía no sé de qué manera te \
    enseñaría. Yo fui una vez tan libre e inocente. Yo también me reía sin motivo. \
    Pero más tarde, tiré por la borda mi tonta inocencia para protegerme. Y luego le \
    enseñé a mi hija, tu madre, a deshacerse de su inocencia para que ella tampoco \
    sufriera daño. Hwai dungsyi, ¿estuvo mal este tipo de pensamiento? Si ahora \
    reconozco el mal en otras personas, ¿no es porque yo también me he vuelto malvada? \
    Si veo que alguien tiene una nariz sospechosa, ¿no he olido yo las mismas cosas \
    malas?" La bebé se rió, escuchando los lamentos de su abuela. "¡Oh! ¡Oh! ¿Dices \
    que te ríes porque ya has vivido para siempre, una y otra vez? ¡Dices que eres \
    Syi Wang Mu, la Reina Madre de los Cielos Occidentales, que has vuelto ahora para \
    darme la respuesta! Bien, bien, te escucho.... Gracias, Pequeña Reina. Entonces \
    debes enseñarle a mi hija esta misma lección. Cómo perder la inocencia, pero no \
    la esperanza. Cómo reír para siempre."'


ref = word_tokenize(reference_text, "spanish")
cand = word_tokenize(candidate_text, "spanish")


# Calculate METEOR score 
score = single_meteor_score(ref, cand)

# Print the result 
print(f"METEOR Score: {score:.4f}")


# %%


