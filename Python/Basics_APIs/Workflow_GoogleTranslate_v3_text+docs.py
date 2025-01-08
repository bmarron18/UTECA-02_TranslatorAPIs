#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025
@author: bmarron

source: translate_v3beta1_translate_document.py
"""


# %%
# [BEGIN Workflow_GoogleTranslate_v3_docs]

'''
Login to Google Cloud account (marron,bruce,mx@gmail,com)
From the Cloud Console, click Activate Cloud Shell 
'''
https://console.cloud.google.com/

Project name
    My Project-UTECA1
Project number
    735387290281
Project ID
    my-project-uteca1


Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to my-project-uteca1.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.

#  Google Cloud Console (w/o IPython)
marron_bruce_mx@cloudshell:~ (my-project-uteca1)$ 

# %%
'''
  Call Google Cloud Translation API
  Authentication
  Follow prompts to obtain new credentials (needed every time)
  Account and Project Configuration
'''
$ gcloud services enable translate.googleapis.com

  # ADC credentials
  # Credentials saved to file: [/tmp/tmp.mIXxB4oSdC/application_default_credentials.json]
$ gcloud auth application-default login


  #check
$ gcloud auth list


$ gcloud config set account 'ACCOUNT'     # <== retype w/ single quotes ''
  # Check
$ 



# %%

'''
    Get the PROJECT_ID environment variable
'''

$ export PROJECT_ID=$(gcloud config get-value core/project)
  #check
$ echo "PROJECT_ID: $PROJECT_ID"
    


# %%

'''
    Create a virtual Python environment on your home computer
    Install IPython and the Translation API client library, google-cloud-translate
    (an SDK)
'''

     # Now from home computer terminal (Linux)
     # cd to same directory as Spyder current working directory (CWD) (/home/bmarron)

$ cd ~
$ virtualenv venv-translate &&
source venv-translate/bin/activate &&
pip install ipython google-cloud-translate


# %%
'''
    Call IPython in Cloud Shell
    Import modules and objects
'''

#  NO!! in Google Cloud Conso
$ export PROJECT_ID=$le (w/o IPython)
# 
$ ipython

import os
#from os import environ
#from os import path
from google.cloud import translate



# %%
'''
  Set variables 
  Define fxn, "translate_document"
'''

#PROJECT_ID = environ.get("PROJECT_ID", "");
PROJECT_ID = " my-project-uteca1";
assert PROJECT_ID ;
PARENT = f"projects/{PROJECT_ID}"

doc_dir = "/home/bmarron/Desktop/UTECA/UTECA_AI_TranslatorSetup/UTECA1_TranslatorAPIs/Python/Basics_APIs" ;
doc_to_translate = "Tester.pdf" ;
file_path = os.path.join(doc_dir, doc_to_translate)

  # set ADC from Google as env variable 
credential_path = "/tmp/tmp.mIXxB4oSdC/application_default_credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def translate_document(
    PARENT: str,
    file_path: str,
) -> translate.TranslationServiceClient:
    
    client = translate.TranslationServiceClient()
    location = "northamerica-south1"
    parent = PARENT
  
    with open(file_path, "rb") as document:
        document_content = document.read()
  
    document_input_config = {
        "content": document_content,
        "mime_type": "application/pdf",
    }

    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": "fr-FR",
            "document_input_config": document_input_config,
        }
    )

    # To output the translated document, uncomment the code below.
    f = open('/tmp/output', 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
    # and its output mime type will be the same as the input file's mime type
    print(
        f"Response: Detected Language Code - {response.document_translation.detected_language_code}"
    )

    return response

# %%

translate_document(PARENT, file_path)

Your default credentials were not found.
 To set up Application Default Credentials, 
 see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.


# %%

'''
TUTORIAL 12
     Clean up
    
'''

In [12]: exit
    # exit Cloud Shell IPython session to go back to the Cloud Shell


$ deactivate
    # Stop using the Python virtual environment on home computer
   
$ cd ~ &&
rm -rf ./venv-translate
    #  Delete your virtual environment folder:on home computer


# [END Workflow_GoogleTranslate_v3_docs]

