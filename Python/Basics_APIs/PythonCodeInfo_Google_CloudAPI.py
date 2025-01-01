#!/usr/bin/env python3
"""
Created on Mon Dec 30 21:54:30 2024

@author: bmarron
"""

# %%

'''
Python code explainations for the tutorial
    Getting Started with Google Cloud Translation API
        https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0
'''

   

# %%

'''
TUTORIAL 6
    Set the PROJECT_ID environment variable (to be used in your application)
'''
export PROJECT_ID=$(gcloud config get-value core/project)
    #Your active configuration is: [cloudshell-22175]
echo "PROJECT_ID: $PROJECT_ID"
    #PROJECT_ID: my-project-uteca1
    
    
    




# %%

'''
TUTORIAL 7 (home computer terminal)
    Create a virtual Python environment on your home computer
    Install IPython and the Translation API client library (an SDK)
'''

$ cd ~
$ virtualenv venv-translate &&
source venv-translate/bin/activate
    # To stop using the virtual environment and go back to your system Python version, 
    # use the "deactivate" command.

$ pip install ipython google-cloud-translate
    # the SDK libraries enable the interface between Google Cloud and home compu


# %%
'''
TUTORIAL 8
 
'''
https://www.geeksforgeeks.org/python-os-environ-object/

    # os            <== a module
    # os.environ    <== an object
    # os,chdir()    <== a method
    
https://docs.python.org/3/library/pprint.html

https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/

# %%

# A python code with pprint 
import requests 
from pprint import pprint 

def geocode(address): 
	url = "https://maps.googleapis.com/maps/api/geocode/json"   # <== need an API key to access 
	resp = requests.get(url, params = {'address': address}) 
	return resp.json() 

# calling the geocode function 
data = geocode('India gate') 

# pretty-printing json response 
pprint(data) 

# %%

import os
os.getcwd()

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

# %%



    #cd() is easy to write using a generator and a decorator.
    # change working directory

    # Option 1  <== USE THIS !!
from contextlib import chdir
with chdir(path):
    
   # Option 2   <== a generator (?)
from contextlib import contextmanager
import os

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

# %%
    # print to file
    # Work within a new directory then go back to the original current working directory

from contextlib import chdir
with chdir('/home/bmarron/Desktop'):
    import pprint
    data = {'a': [1, 2, 3], 'b': {'c': 4, 'd': 5}}

    with open('output.txt', 'w') as f:
        pprint.pprint(data, stream=f)
    
    with open('out.txt', 'w') as f:
        print('Data', data, file=f)
        

print(os.getcwd())
    
# %%

# importing os module  
import os 
import pprint 
  
# Get the list of user's 
env_var = os.environ 
  
# Print the list of user's 
print("User's Environment Variables:") 
pprint.pprint(dict(env_var), width = 1)
    
    
    
# %%
    
from os import environ
from google.cloud import translate


PROJECT_ID = environ.get("PROJECT_ID", "")
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"

# %%

'''
TUTORIAL 9
    
'''

$ def print_supported_languages(display_language_code: str):
    client = translate.TranslationServiceClient()

    response = client.get_supported_languages(
        parent=PARENT,
        display_language_code=display_language_code,
    )

    languages = response.languages
    print(f" Languages: {len(languages)} ".center(60, "-"))
    for language in languages:
        language_code = language.language_code
        display_name = language.display_name
        print(f"{language_code:10}{display_name}")


print_supported_languages("en")
---------------------- Languages: 194 ----------------------
ab        Abkhaz
ace       Acehnese
ach       Acholi
af        Afrikaans
sq        Albanian
alz       Alur
am        Amharic
ar        Arabic
hy        Armenian
as        Assamese
...
yua       Yucatec Maya
zu        Zulu

# %%

#def function_name(parameter1: type1, parameter2: type2) -> return_type:
    # function body
    return value

    #Example

#def add_numbers(x: int, y: int):
#     return (x + y)

def get_even(numbers):
    
    even_nums = [num for num in numbers if not num % 2]
    return even_nums

get_even([1, 2, 3, 4, 5, 6])


'''
In this example:

    x: int and y: int indicate that the parameters x and y are expected to be integers.
    -> int indicates that the function will return an integer value.
   . 
'''

# %%

'''
TUTORIAL 10
    https://www.google.com/search?q=Function+annotation+%28indicates+the+return+type+of+a+function%29&sca_esv=283076fa18b0ec9a&sxsrf=ADLYWIIH4Q1BZXaazXgd-5JLWpl3mjQ1gw%3A1735700114610&source=hp&ei=kq50Z7yxI7Kw0PEPo6P68A8&iflsig=AL9hbdgAAAAAZ3S8ovfvhI9kydzEOhyV_gKZNB5_x3Gx&ved=0ahUKEwi8wpDmwtOKAxUyGDQIHaORHv4Q4dUDCBs&uact=5&oq=Function+annotation+%28indicates+the+return+type+of+a+function%29&gs_lp=Egdnd3Mtd2l6Ij1GdW5jdGlvbiBhbm5vdGF0aW9uIChpbmRpY2F0ZXMgdGhlIHJldHVybiB0eXBlIG9mIGEgZnVuY3Rpb24pSABQAFgAcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAvgBAZgCAKACAJgDAOIDBRIBMSBAkgcAoAcA&sclient=gws-wiz
'''

def translate_text(text: str, target_language_code: str) -> translate.Translation:
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        parent=PARENT,
        contents=[text],
        target_language_code=target_language_code,
    )

    return response.translations[0]

# %%

'''
TUTORIAL 11
    
'''

text = "Hello World!"
target_languages = ["tr", "de", "es", "it", "el", "zh", "ja", "ko"]

print(f" {text} ".center(50, "-"))
for target_language in target_languages:
    translation = translate_text(text, target_language)
    source_language = translation.detected_language_code
    translated_text = translation.translated_text
    print(f"{source_language} → {target_language} : {translated_text}")

------------------ Hello World! ------------------
en → tr : Selam Dünya!
en → de : Hallo Welt!
en → es : ¡Hola Mundo!
en → it : Ciao mondo!
en → el : Γεια σου Κόσμο!
en → zh : 你好世界！
en → ja : 「こんにちは世界」
en → ko : 안녕하세요!


text = "What the fuck!"

print(f" {text} ".center(50, "-"))
for target_language in target_languages:
    translation = translate_text(text, target_language)
    source_language = translation.detected_language_code
    translated_text = translation.translated_text
    print(f"{source_language} → {target_language} : {translated_text}")
    
----------------- what the fuck! -----------------
en → tr : ne oluyor lan!
en → de : was zur Hölle!
en → es : ¡Qué carajo!
en → it : che cazzo!
en → el : τι στο διάολο!
en → zh : 什么鬼！
en → ja : 何だこれ！
en → ko : 이게 뭐야!


# %%

'''
TUTORIAL 12
     Clean up
    
'''

In [12]: exit
    # exit Cloud Shell IPython session to go back to the Cloud Shell


$ deactivate
    # Stop using the Python virtual environment on home computer
   
$ cd ~
$ rm -rf ./venv-translate
    #  Delete your virtual environment folder:on home computer

To delete your Google Cloud project, from Cloud Shell:
    Retrieve your current project ID: PROJECT_ID=$(gcloud config get-value core/project)
    Make sure this is the project you want to delete: echo $PROJECT_ID
    Delete the project: gcloud projects delete $PROJECT_ID

# %%



