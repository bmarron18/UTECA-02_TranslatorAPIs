#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:54:30 2024

@author: bmarron
"""

# %%


'''
Google offers
    DeepL
    Cloud Translation API
'''

'''
Google DeepL
https://transcy.crisp.help/en/article/how-to-translate-target-language-by-deepl-service-1ftwdt4/?bust=1712201846082

'''
# %%

'''
Google Cloud Translation API
https://cloud.google.com/translate/?hl=en

Cloud Translation API uses Google's neural machine translation technology to let 
you dynamically translate text through the API using a Google pre-trained, custom model, or a 
translation specialized large language model (LLMs). 

It comes in Basic (v2) and Advanced (v3) editions. Both provide fast and dynamic translation, but Advanced 
offers customization features, such as domain-specific translation, formatted document translation, 
and batch translation. 

The first 500,000 characters sent to the API to process (Basic and Advanced 
combined) per month are free (not applicable to LLMs).


Model selection
For advanced translations, you're not limited to a one-size-fits-all solution, ensuring the highest 
quality and accuracy for your specific content. You can choose from the following models, based on 
your needs: 
  a) Neural Machine Translation (NMT) for general text in everyday use cases like website content or news 
articles; 

b) Translation Large Language Model (LLM) for conversational text like messages or social media posts. 
You can use "Adaptive" mode to fine-tune translations based on your own examples for an even closer 
match to your unique style.


'''


# %%

'''
 Google Cloud Translation API with Python
'''

      
  # Cloud Client Libraries
https://cloud.google.com/apis/docs/cloud-client-libraries
https://cloud.google.com/apis/docs/client-libraries-explained
https://developers.google.com/api-client-library/
https://developers.google.com/apis-explorer/
 

  # Cloud Client Libraries -- Python
https://cloud.google.com/python
 https://github.com/googleapis/google-cloud-python
https://cloud.google.com/python/docs/getting-started
https://cloud.google.com/python/docs/setup
https://cloud.google.com/python/docs/reference


  # Cloud Client Libraries -- Translation
https://cloud.google.com/translate/docs
https://cloud.google.com/translate/docs/setup
https://cloud.google.com/translate/docs/reference/rest
https://cloud.google.com/translate/docs/supported-formats
https://pypi.org/project/google-cloud-translate/


  # Cloud Client Librariesn  -- Translation w/ Python
https://cloud.google.com/python/docs/reference/translate/latest
https://cloud.google.com/translate/docs/advanced/translating-text-v3#translate_v3_translate_text-python
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/translate/samples/snippets
      
  # Google Zones and Location of Servers for Cloud Computing
https://cloud.google.com/compute/docs/regions-zones

  #Spyder IDE
https://docs.spyder-ide.org/5/faq.html#using-packages-installer

# %%

# new cells  (Ctrl+2)




# %%


'''

Getting Started with Google Cloud Translation API
    USE THIS TUTORIAL!!
    '''
    
 https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0


# %%

'''
TUTORIAL 1
    Create a Google Cloud account and log in
'''
https://console.cloud.google.com/

'''
Log in to https://console.cloud.google.com/

Welcome, Bruce Marron
Try Google Cloud with $300 in free credits

Access to Google Cloud products and services
90 days to spend your credits
No billing during trial

You have 12 projects remaining in your quota.
Next, you'll need to enable billing in the Cloud Console to use 
Cloud resources/APIs. Running through this codelab won't cost much, if 
anything at all. To shut down resources to avoid incurring billing beyond 
this tutorial, you can delete the resources you created or delete the project. 
New Google Cloud users are eligible for the $300 USD Free Trial program.
'''

Project name
    My Project-UTECA1
Project number
    735387290281
Project ID
    my-project-uteca1 


# %%

'''
TUTORIAL 2
     From the Cloud Console, click Activate Cloud Shell 
'''

'''
Google Cloud Shell is an IDE with a command line interface. This virtual machine is loaded with all the 
development tools needed. It offers a persistent 5 GB home directory and runs in Google Cloud.

Cloud Shell is a Debian-based virtual machine 
'''

Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to my-project-uteca1.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
marron_bruce_mx@cloudshell:~ (my-project-uteca1)$ 
    
    
# %%

'''
TUTORIAL 3
     Authentication
'''
    #  in Google Cloud Console (w/o IPython)

 $ gcloud auth login
     # to obtain new credentials.
     # follow prompts to obtain new credentials (needed every time)

$ gcloud auth list
    #Cloud Shell needs permission to use your credentials for the gcloud CLI command.
    #Click Authorize to grant permission to this and future calls. 
    # NB --- need to activate Free Trial to authenticate account
    
    #ACTIVE: *
    #ACCOUNT: marron.bruce.mx@gmail.com

# %%

'''
TUTORIAL 4
     Account and Project Configuration
'''
    #  in Google Cloud Console (w/o IPython)

$ gcloud config set account 'ACCOUNT'     # <== retype w/ single quotes ''

$ gcloud config list project
 

# %%

'''
TUTORIAL 5
    Call Google Cloud Translation API
'''

#  in Google Cloud Console (w/o IPython)

$ gcloud services enable translate.googleapis.com
    # Operation "operations/acat.p2-735387290281-9ce6663f-72ab-40a2-84f7-5c5802490b1a" 
    # finished successfully.
   

# %%

'''
TUTORIAL 6
    Set the PROJECT_ID environment variable (to be used in your application)
'''
https://stackoverflow.com/questions/35599414/get-the-default-gcp-project-id-with-a-cloud-sdk-cli-one-liner

#  in Google Cloud Console (w/o IPython)


$ export PROJECT_ID=$(gcloud config get-value core/project)
    #Your active configuration is: [cloudshell-22175]
$ echo "PROJECT_ID: $PROJECT_ID"
    #PROJECT_ID: my-project-uteca1
    


# %%

'''
TUTORIAL 7 
    Create a virtual Python environment on your home computer
    Install IPython and the Translation API client library (an SDK)
'''

     # in home computer terminal (Linux) 

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
    Call IPython in Cloud Shell
    Import objects 'os.environ' and 'google.cloud.translate'
'''

#  in Google Cloud Console (w/ IPython)
$ ipython

   # OS Environment variables (sometimes called "env vars") are variables you store outside your
   # program that can affect how it runs. For example, you can set environment variables that
   # contain the key and secret for an API. Your program might then use those variables when it 
   # connects to the API. 
   
   # os.environ is a mapping object that maps the user's environmental variables. It returns a 
   # dictionary or table having the user's environmental variable as key and their values as value.
   # os. environ behaves like a common dictionary, so operations like get and set can be performed


#  in Google Cloud Console (w/ IPython)

>>> from os import environ
>>> from google.cloud import translate

>>> PROJECT_ID = environ.get("PROJECT_ID", "")
>>> assert PROJECT_ID
>>> PARENT = f"projects/{PROJECT_ID}"

# %%

'''
TUTORIAL 9
'''

#  in Google Cloud Console (w/ IPython)


>>> def print_supported_languages(display_language_code: str):
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


>>> print_supported_languages("en")
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

'''
TUTORIAL 10
'''

#  in Google Cloud Console (w/ IPython)

>>> def translate_text(text: str, target_language_code: str) -> translate.Translation:
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        parent=PARENT,
        contents=[text],
        target_language_code=target_language_code,
    )

    return response.translations[0]



>>> text = "Hello World!"
>>> target_languages = ["tr", "de", "es", "it", "el", "zh", "ja", "ko"]
>>> print(f" {text} ".center(50, "-"))


>>> for target_language in target_languages:
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



