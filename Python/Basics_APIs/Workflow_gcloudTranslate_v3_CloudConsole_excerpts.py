#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025
@author: bmarron

source: translate_v3beta1_translate_document.py
"""


# %%
# [BEGIN Workflow_gcloudTranslate_v3_CloudConsole_excerpts]

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

'''
#  Google Cloud Console (w/o IPython)
marron_bruce_mx@cloudshell:~ (my-project-uteca1)$ 

Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to my-project-uteca1.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.


'''
# %%
'''
Doing simple translations in Google Cloud Console
  Call Google Cloud Translation API
  Authentication
  Follow prompts to obtain new credentials (needed every time)
  Account and Project Configuration
'''
$ gcloud services enable translate.googleapis.com

  # ADC credentials ONLY if working in Cloud Shell!!
  # Credentials saved to file: [/tmp/tmp.mIXxB4oSdC/application_default_credentials.json]
$ gcloud auth application-default login


  #check
$ gcloud auth list


$ gcloud config set account 'ACCOUNT'     # <== retype w/ single quotes ''
  # Check
$ 



# %%

'''
Doing simple translations in Google Cloud Console
    Get the PROJECT_ID environment variable
'''

$ export PROJECT_ID=$(gcloud config get-value core/project)
  #check
$ echo "PROJECT_ID: $PROJECT_ID"
    

# %%

'''
Doing full doc translations via local machine
  Install gcloud CLI or SDK on local machine
'''
google-cloud-cli-linux-x86_64.tar.gz

# %%

'''
Doing full doc translations via local machine
    Create a virtual Python environment on your home computer
    Install IPython and the Translation API client library, google-cloud-translate
    (an SDK)
'''

     # Now from home computer terminal (Linux)
     # cd to same directory as Spyder current working directory (CWD) (/home/bmarron)

$ cd ~ &&
./google-cloud-sdk/bin/gcloud auth application-default login


$ ./google-cloud-sdk/bin/gcloud auth application-default login
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login&state=RsXzAq0LHb8C1eSOuI4UxZRLI8TReo&access_type=offline&code_challenge=08jR7ncGpVzDXiyMs90opsGlu75RhOGZQF3ZBw-wLnU&code_challenge_method=S256


Credentials saved to file: [/home/bmarron/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).
WARNING: 
Cannot find a quota project to add to ADC. You might receive a "quota exceeded" or "API not enabled" error. Run $ gcloud auth application-default set-quota-project to add a quota project.



 
$ cd ~ 
$ virtualenv venv-translate &&
source venv-translate/bin/activate &&
pip install ipython google-cloud-translate



# %%
'''
Doing full doc translations via local machine
    Call IPython in venv 
    Import modules and objects
'''

$ ipython

import os
#from os import environ
#from os import path
from google.cloud import translate



# %%
'''
Doing full doc translations via local machine
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

