#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025
@author: bmarron

source: translate_v3beta1_translate_document.py
"""

# %%

=======   Preliminaries   ===========================

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
Install gcloud SDK on home compu 
    [==> /home/bmarron/google-cloud-sdk]
'''
https://cloud.google.com/sdk/docs/install
    google-cloud-cli-linux-x86_64.tar.gz

  # Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.
$ cd ~
$ ./google-cloud-sdk/bin/gcloud cheat-sheet




# %%
'''
Check for google-cloud-sdk updates
Revert google-cloud-sdk to previous version (if needed)
'''
    
$ cd ~
$ ./google-cloud-sdk/bin/gcloud components update



To revert your CLI to the previously installed version:
  $ gcloud components update --version 505.0.0
 
 


# %%
'''
Initial attempts at using Spyder for Google Cloud APIs
(tricky!)

SKIP THIS....FYI ONLY
'''

---- Options
    1, Link google-cloud-sdk to Spyder python interpreter
    2. Link Spyder to google-cloud-sdk Python
    3. Install spyder kernels in virtenv  <==This one!!

Messed with all of these...uff! Until found option 3. above
Had to go back and re-set....uff
Here's a variety of websites and info 



---- There are multiple Python distros on my compu
    # The default google-cloud-sdk bundled Python interpreter is here:
/home/bmarron/google-cloud-sdk/platform/bundledpythonunix/bin/python3.12

    # The default Spyder python interpreter is here:
/home/bmarron/.local/spyder-6/bin/python3.11
OR
/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/

    # LinuxMint's python interpreter is here
/usr/lib/python2.7
/usr/lib/python3


---- $PYTHONPATH
https://askubuntu.com/questions/384996/what-does-my-pythonpath-contain

Typically, the environment variable $PYTHONPATH is empty 
$ echo $PYTHONPATH

The actual list of folders python searches for libraries can be found
 with

import sys
print(sys.path)

['/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python311.zip', 
 '/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11', 
 '/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11/lib-dynload', 
 '', '/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages']




---- Google has installed LOTS of API site packages here
/home/bmarron/.local/lib/python3.10/site-packages/google
/home/bmarron/.local/lib/python3.10/site-packages/google_api_core-2.24.0.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/google_auth-2.37.0.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/google_cloud_core-2.4.1.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/google_cloud_translate-3.19.0.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/googleapis_common_protos-1.66.0.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/grpc
/home/bmarron/.local/lib/python3.10/site-packages/grpc_google_iam_v1-0.13.1.dist-info
/home/bmarron/.local/lib/python3.10/site-packages/grpc_status
...



---- DO NOT USE!!
#To change Python interpreter in Spyder
# select an option
#     Internal 
#     Use the following Python interpreteruse the dropdown below to select your preferred environment.
#     /home/bmarron/google-cloud-sdk/platform/bundledpythonunix/bin/python3.12
#NO GO!!
#An error occurred while starting the kernel
#The Python environment or installation whose interpreter is located at
#    /home/bmarron/google‑cloud‑sdk/platform/bundledpythonunix/bin/python3
#doesn't have spyder‑kernels version >=3.0.0,<3.1.0 installed. Without this module and 
#specific version is not possible for Spyder to create a console for you. You can install it by 
#activating your environment (if necessary) and then running in a system terminal:
#    conda install spyder-kernels=3.0
#or


---- Option 3: pip install spyder-kernels==3.0.* in virtual environment
https://stackoverflow.com/questions/30170468/how-to-run-spyder-in-virtual-environment

The modular approach
1- Activate the environment (e.g. myenv) in which you'd like to work
 (e.g. source myenv/bin/activate or workon myenv for virtualenv/venv, etc)

2- Install the spyder-kernels package there, with the command if using pip/virtualenv.
    pip install spyder-kernels 

3- After installing via either method, run the following command inside
 the same environment:
     python -c "import sys; print(sys.executable)"    

and copy the path returned by that command 
it should end in python, pythonw, python.exe or pythonw.exe, depending on your operating system).

4- start Spyder as you normally would.

5- After Spyder has started, navigate to Tools > Preferences > Python Interpreter > Use the following interpreter
paste the path from Step 3 into the text box.

6- Start a new IPython console. 




---- trying to install google-cloud-translate in Spyder Python

https://stackoverflow.com/questions/59200541/why-does-my-google-translate-api-work-in-the-terminal-but-not-an-executable
https://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip
https://stackoverflow.com/questions/44389630/using-spyder-with-virtualenv


---- how to re-configure google-cloud-sdk Python interpreter
$ cd ~
$ ./google-cloud-sdk/bin/gcloud topic startup


---- tried this 
   #set the CLOUDSDK_PYTHON environment variable to Spyder default python interpreter
$ export CLOUDSDK_PYTHON=/home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11
$ pip install --target /home/bmarron/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/ google-cloud-translate


---- tried this
Install google-cloud-translate; Spyder kernels in LinuxMint Python 3.10thon

    # Set Spyder [Tools ==> Preferences ==> Python Interprepter]
 /home/bmarron/.local/spyder-6/bin/python3.11

$ export PYTHONPATH=${PYTHONPATH}:${HOME}/.local/spyder-6/bin/python3.11
$ export CLOUDSDK_PYTHON=/home/bmarron/.local/spyder-6/bin/python3.11
$ pip install --target /home/bmarron/.local/lib/python3.10/site-packages/ google-cloud-translate

import sys
sys.path.append('/home/bmarron/.local/lib/python3.10/site-packages/')

 

---- Re-sets
    # Use the python3 interpreter on your path
$ export CLOUDSDK_PYTHON=python3



# %%
'''
   Obtain Application Default Credentials (ADC)
   (Only once; stored as .json file)
'''

  # Initial get of ADC credentials 
  # will be stored locally as .json file
  # ADC authentication is thru google-cloud-sdk 
  # Browser sent to Google Auth Library; follow browser prompts
  # NOT setting up a Service Account; ADC stored locally
  # once have credentials will be used by any library that requests ADCs
 
$ cd ~
$ ./google-cloud-sdk/bin/gcloud auth application-default login


   
    # ADC credentials are saved here:: 
/home/bmarron/.config/gcloud/application_default_credentials.json



# %%
'''
Check the authentication account used by gcloud
Set the authentication account (if needed)
'''
    #Check current authentication account
$ cd ~
$ ./google-cloud-sdk/bin/gcloud auth list

      Credentialed Accounts
ACTIVE  ACCOUNT
*       marron.bruce.mx@gmail.com


    # set the authentication account (if needed)
$ gcloud config set account `ACCOUNT`   #<== re-type 'ACCOUNT' w/ apostrophes!!



# %%
'''
Set Google Cloud projects for billing and quotas
(Only once per project)
'''

    # quotas are per project
    #  set to "my-project-uteca1"
$ ./google-cloud-sdk/bin/gcloud auth application-default set-quota-project my-project-uteca1

Quota project "my-project-uteca1" was added to ADC which can be used by 
Google client libraries for billing and quota.



# %%

============== Workflow_gcloudAPI_StandardNMT_GeneralTranslation_docs.py  ============

# %%

'''
Doing complete document translations thru API with the Standard NMT model
  Account and Project Configuration
  (Re-set every session)
'''

  # sign in and follow prompts for account and project config
  #  ==> follow prompts
$ cd ~ 
$ ./google-cloud-sdk/bin/gcloud init

Welcome! This command will take you through the configuration of gcloud.....

The Google Cloud CLI is configured and ready to use!


  
# %%

'''
    Create a virtual Python environment on local machine (home computer)
      ==> Install IPython
      ==> Install the SDK for Google language translation (google-cloud-translate)
      ( aka the Google Translation API client library)
      ==> spyder kernels
'''
 
$ cd ~ 
$ virtualenv venv-translate &&
source venv-translate/bin/activate &&
pip install spyder-kernels ipython google-cloud-translate

    # terminal now here
(venv-translate) bmarron@bmarron-HP-Laptop-15t-dy100:~$ 


# %%
'''
Getting Spyder into venv-translate
'''


$ python -c "import sys; print(sys.executable)"
    /home/bmarron/venv-translate/bin/python  

    # in spyder
Tools > Preferences > Python Interpreter > Use the following interpreter
paste the path and then the file above into text box

6- Start a new IPython console. 

# %%
'''
    Call IPython in venv 
    Import modules
      ==> os
      ==> google.cloud.translate (SDK) translation fxn
'''

import os
#from google.cloud import translate
from google.cloud import translate_v3 as translate


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
# %%
'''
set target language variable for translation
'''

target = "hi"



# %%


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
translate_document(project_id, file_path)


# %%

  # Model used by Google to do the translation
  # Neural Machine Translation (NMT)
  
model: "projects/735387290281/locations/us-central1/models/general/nmt"

# %%

'''
  Clean up
'''
    # exit Cloud Shell IPython session (if working in terminal)
In [12]: exit

    # re-set spyder to original python interpreter

   

   # Stop using the Python virtual environment 
$ deactivate
   
   # Delete virtual environment folder (local machine)
$ cd ~ &&
rm -rf ./venv-translate
    


# [END Workflow_GoogleTranslate_v3_docs]

