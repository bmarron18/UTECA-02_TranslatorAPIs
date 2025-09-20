# %%
# -*- coding: utf-8 -*-

"""
Spyder Editor

"""

'''
https://platform.openai.com/docs/quickstart

https://community.openai.com/t/which-api-for-translation/553000/6
https://platform.openai.com/docs/api-reference/responses

https://platform.openai.com/docs/api-reference/responses/create
https://platform.openai.com/docs/guides/migrate-to-responses
https://platform.openai.com/docs/guides/pdf-files?api-mode=responses

https://community.openai.com/t/translation-script-not-working/896719/2
https://platform.openai.com/docs/api-reference/chat/create?lang=python

'''
# %%

    # Response API usage	<== USE THIS for .pdf / .txt translation!!
    # Install OpenAI SDK into conda env, (spyder_env)
    
$ conda activate spyder_env
(spyder_env)$ conda install openai
(spyder_env)$ conda deactivate



# %%

'''
Simple Test Run

'''

from openai import OpenAI

#client = OpenAI(api_key=API_KEY)
client = OpenAI(api_key="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")

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

	# Upload a .pdf / .txt referenced in input = []
file = client.files.create(
    file=open("draconomicon.pdf", "rb"),
    purpose="user_data",
)


# %%


from openai import OpenAI
from pathlib import Path
import os


#client = OpenAI(api_key=API_KEY)
client = OpenAI(api_key="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")



# --- Define Files and File Paths ---
    # Create one (1) empty file on the Desktop
        # ==> OUTPUT_FILE will hold the Translated text from the AI
        # ==> file extension must be .pdf
    # Select .pdf file to be translated and place in Desktop
        # ==> INPUT_FILE will hold the .pdf To Be Translated

    # watch file name for INPUT_FILE
        # ==> strictly alpha! 
        # ==> NO dashes or underline (won't upload to Gemini)
    
    # Change the language names in the files as needed
    # Change the file extension of OUTPUT_FILE as needed
    
INPUT_FILE = "englishTBT.pdf"  
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



	# Upload a .txt referenced in input = []
file = client.files.create(
    file=open(filepath, "rb"),
    purpose="user_data",
)

	# Developer level
sys_prompt = "You are a linguistics expert specializing in translations. \
    Do not provide additional commentary. Just perform the task at hand."

	# User level
user_prompt= "Translate the uploaded file to standard Spanish."



	# API call
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

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(response.output_text)
     
print(f"Translation complete! Translated text saved to '{output_filepath}'.")


