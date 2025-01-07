#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025

@author: bmarron
"""


# %%
# [BEGIN Workflow_GoogleTranslate_v3_docs]

'''
Login to Google Cloud account
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
  Authentication
  Follow prompts to obtain new credentials (needed every time)
  Account and Project Configuration
'''

$ gcloud auth login
$ gcloud auth list


$ gcloud config set account 'ACCOUNT'     # <== retype w/ single quotes ''
$ gcloud config list project


# %%

'''
  Call Google Cloud Translation API
'''

$ gcloud services enable translate.googleapis.com


# %%

'''
    Get the PROJECT_ID environment variable
'''

$ export PROJECT_ID=$(gcloud config get-value core/project)
$ echo "PROJECT_ID: $PROJECT_ID"
    


# %%

'''
    Create a virtual Python environment on your home computer
    Install IPython and the Translation API client library, google-cloud-translate
    (an SDK)
'''

     # in home computer terminal (Linux) 

$ cd ~
$ virtualenv venv-translate &&
source venv-translate/bin/activate
 
$ pip install ipython google-cloud-translate


# %%
'''
TUTORIAL 8
    Call IPython in Cloud Shell
    Import objects 'os.environ' and 'google.cloud.translate'
'''

#  in Google Cloud Console (w/o IPython)
$ ipython

#  in Google Cloud Console (w/ IPython)
from os import environ
from google.cloud import translate

PROJECT_ID = environ.get("PROJECT_ID", "")
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"

# %%

def translate_document(
    project_id: str,
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
    # f = open('/tmp/output', 'wb')
    # f.write(response.document_translation.byte_stream_outputs[0])
    # f.close()

    # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
    # and its output mime type will be the same as the input file's mime type
    print(
        f"Response: Detected Language Code - {response.document_translation.detected_language_code}"
    )

    return response





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


# [END Workflow_GoogleTranslate_v3_docs]

