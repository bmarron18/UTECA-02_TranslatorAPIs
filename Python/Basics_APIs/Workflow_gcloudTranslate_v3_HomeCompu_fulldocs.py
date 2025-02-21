#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025
@author: bmarron

source: translate_v3beta1_translate_document.py
"""

# %%

# [BEGIN Workflow_gcloudTranslate_v3_fr-compu.docs]
  # ==> Preliminaries

# %%

'''
Login to Google Cloud account (marron,bruce,mx@gmail,com)
Activate Cloud Shell 
Check account status and exit
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

    #  Google Cloud Console shell
marron_bruce_mx@cloudshell:~ (my-project-uteca1)$ 

# %%

'''
Install gcloud CLI (or SDK) on home compu in /home/bmarron
'''
google-cloud-cli-linux-x86_64.tar.gz

  # Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.
$ cd ~
$ ./google-cloud-sdk/bin/gcloud cheat-sheet

# %%
'''
   Obtain initial Application Default Credentials (ADC)
   ADC authentication is thru google-cloud-sdk 
   (browser sent to Google Auth Library; follow browser prompts)
  [NB. NOT setting up a Service Account; ADC stored locally]
'''
  # get ADC credentials (stored locally as .json file)
$ cd ~
$ ./google-cloud-sdk/bin/gcloud auth application-default login

''' Credentials saved to file: 
[/home/bmarron/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests 
Application Default Credentials (ADC).'''

    # set quota to "my-project-uteca1" in ADC credentials  
$ ./google-cloud-sdk/bin/gcloud auth application-default set-quota-project my-project-uteca1

'''Quota project "my-project-uteca1" was added to ADC which can be used by 
Google client libraries for billing and quota.'''




# %%

# [BEGIN Workflow_gcloudTranslate_v3_fr-compu.docs]
  # ==> Normal workflow
'''
  Account and Project Configuration
'''

  # sign in and follow prompts for account and project config
  #  ==> follow prompts
$ cd ~ 
$ ./google-cloud-sdk/bin/gcloud init

'''The Google Cloud CLI is configured and ready to use
Created a default .boto configuration file at [/home/bmarron/.boto]. 
The Google Cloud CLI is configured and ready to use!'''

  
# %%

'''
    Create a virtual Python environment on local machine (home computer)
      ==> Install IPython
      ==> Install the SDK for Google language translation (google-cloud-translate)
      ( aka the Google Translation API client library)
'''
 
$ cd ~ 
$ virtualenv venv-translate &&
source venv-translate/bin/activate &&
pip install ipython google-cloud-translate



# %%
'''
    Call IPython in venv 
    Import modules
      ==> os
      ==> google.cloud.translate (SDK)
'''

$ ipython

import os
from google.cloud import translate



# %%
'''
  Set variables 
  Define the translation fxn, "translate_document"
'''
  # Google Cloud project used for translation work
PROJECT_ID = "my-project-uteca1";
assert PROJECT_ID ;
project_id = PROJECT_ID

  # path to document for translation
doc_dir = "/home/bmarron/Desktop/UTECA/UTECA_AI_TranslatorSetup/UTECA1_TranslatorAPIs/Python/Basics_APIs" ;
doc_to_translate = "Tester.pdf" ;
file_path = os.path.join(doc_dir, doc_to_translate)

  # set ADC from Google as a Python env variable 
credential_path = "/home/bmarron/.config/gcloud/application_default_credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

  # set target language for translation
target = "ja"

  # the translation fxn: single doc to single language
def translate_document(
    project_id: str,
#    PROJECT_ID,
    file_path: str,
) -> translate.TranslationServiceClient:
    
    client = translate.TranslationServiceClient()
    location = "us-central1"
    parent = f"projects/{project_id}/locations/{location}"
    
   
    with open(file_path, "rb") as document:
        document_content = document.read()
  
    document_input_config = {
        "content": document_content,
        "mime_type": "application/pdf",
    }

    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": target,
            "document_input_config": document_input_config,
        }
    )

    # To output the translated document, uncomment the code below.
    f = open('/home/bmarron/Desktop/gcTranslate_output_ja.pdf', 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
    # and its output mime type will be the same as the input file's mime type
    print(
        f"Response: Detected Language Code - {response.document_translation.detected_language_code}"
    )

    return response

# %%

  # Do the translation
$ translate_document(project_id, file_path)

  # Model used by Google to do the translation
  # Neural Machine Translation (NMT)
model: "projects/735387290281/locations/us-central1/models/general/nmt"
model: "projects/735387290281/locations/us-central1/models/general/nmt"
# %%

'''
  Clean up
    '''
    # exit Cloud Shell IPython session
In [12]: exit
   

   # Stop using the Python virtual environment 
$ deactivate
   
   # Delete virtual environment folder (local machine)
$ cd ~ &&
rm -rf ./venv-translate
    


# [END Workflow_GoogleTranslate_v3_docs]

