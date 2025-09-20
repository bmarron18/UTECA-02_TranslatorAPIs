# %%
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 19 2025
@author: bmarron


"""

# %%

'''
Simple Test Run

'''

import os
from openai import OpenAI

    # API_KEY is saved as an ENV VARIABLE on home compu
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

    # API_KEY is inserted directly
#client = OpenAI(api_key=ACTUAL_API_KEY)


response = client.responses.create(
  model = "gpt-4o",
  temperature = 1.3,
  instructions = "Talk like a pirate.",
  input = "Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

'''
Arr matey, once upon a time, atop the moonlit waves o' dreamland, pranced a 
shimmering unicorn, whose horn sparkled with such magic it sent the young 
pirate driftin' to sleep among the stars.
'''



# %%

'''
Translate content of .pdf files w/o uploading to OpenAI's Vector Store
    * returns UTF-8 output (a text file)
    * output may be requested as a .txt or .tex file

'''


from openai import OpenAI
from pathlib import Path
import os

    # API_KEY is saved as an ENV VARIABLE on home compu
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

    # API_KEY is inserted directly
#client = OpenAI(api_key=ACTUAL_API_KEY)




# --- Define Files and File Paths ---
    # Create one (1) empty file on the Desktop, the OUTPUT_FILE
        # ==> OUTPUT_FILE will hold the (T)ranslated text from the AI
        # ==> set file extension to .txt unless requesting a .tex file

    # Select .pdf file to be translated and place on the Desktop
        # ==> INPUT_FILE will hold the .pdf file (T)o (B)e (T)ranslated

      
    # Change the language names in the files as needed
    # Change the file extension of OUTPUT_FILE as needed
    
INPUT_FILE = "englishTBT.pdf"  
OUTPUT_FILE = "spanish_T.txt"
    
    
    # set up the file paths for the INPUT_FILE and the OUTPUT_FILE
    # set the file path to your Desktop
    # Path() represents file+directory paths in a platform-independent manner.
    
doc_to_translate = INPUT_FILE
doc_to_print = OUTPUT_FILE
doc_dir = "/home/bmarron/Desktop"


    # create paths to files
    # Retrieve files as PosixPaths

input_filepath = os.path.join(doc_dir, doc_to_translate)
input_f = Path(input_filepath)

output_filepath = os.path.join(doc_dir, doc_to_print)
output_f = Path(output_filepath)


    

	# Read the .pdf INPUT_FILE (now named, input_f)
file = client.files.create(
    file=open(input_f, "rb"),
    purpose="user_data",
)

	# Developer level message
sys_prompt = "You are an expert liguist \
    specializing in translation. Maintain the original \
    meaning and tone. Provide ONLY the requested translation without \
    any additional commentary, introductory phrases, other language \
    translations or conversational remarks."

	# User level message
user_prompt= "Translate the .pdf file (in English) to standard, natural, \
    and fluent Spanish. Maintain all specific formatting (line breaks, \
    indents, spaces, paragraphs)."




	# Response API call
response = client.responses.create(
    model="gpt-4o",
    temperature=1.3,
    instructions= sys_prompt,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": user_prompt,
                },
            ]
        }
    ]
)

	# API output to IPython
#print(response.output_text)


#--- Output to OUTPUT_FILE---

with open(output_f, "w", encoding="utf-8") as f:
     f.write(response.output_text)
     
print(f"Translation complete! Translated text saved to '{output_f}'.")


