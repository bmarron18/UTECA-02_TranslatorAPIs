#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 06 Jan 2025
Modified: 25 Jan 2025
@author: bmarron

sources: 
*translate_v3beta1_translate_document.py
*https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient
*https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_document
*https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_document
"""


# %%

====    Windows Preliminaries and Background Info    ==========================

# %%

    #change the directory to root using
> cd\


    # change to home directory
> cd %homedrive%%homepath%

# %%

'''
Open terminal
'''
Click the Start menu and type "cmd" in the search bar to 
find the Command Prompt. 


To open a terminal in a specific folder on Windows 10, navigate to the 
desired folder in File Explorer, then hold down the Shift key, right-click
 within the folder, and select "Open in terminal" from the context menu. 

# %%
'''
Install Notepad++
'''

C:\Program Files\Notepad++


# %%

'''
    Search Windows dorectories
'''
https://stackoverflow.com/questions/8066679/how-to-do-a-simple-file-search-in-cmd

    #searches in current folder and sub folders.
    # finds directories as well as files
    # wildcards * like Linux
    # /s Lists every occurrence of the specified file name within the specified directory and all subdirectories.
    # printo text file

> dir /b/s *foo* 

    # -d excludes directories
    # /a: 
> dir /a:-d /b/s *foo* >> file.txt



    #List all Hidden Files
> dir /a:h-d /b/s

    #List all System Files
> dir /a:s-d /b/s

    List all ReadOnly Files
> dir /a:r-d /b/s

    # List all Non Indexed Files
> dir /a:i-d /b/s

# %%

'''
    Search ALL Windows dorectories for Pyhton
'''
C:\Users\bmarr\> cd\
C:\> 

C:\> dir /b/s *python* >>C:\Users\bmarr\Desktop\python.txt

# %%

'''
    Search C:\ for pyhton.exe
'''
C:\Users\bmarr\> cd\
C:\> 

C:\> dir /b/s python.exe >> C:\Users\dassn\OneDrive\Escritorio\python_exe_files.txt


    # google-cloud-sdk bundled python 
    #    ==> Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
C:\Users\bmarr\AppData\Local\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython\python.exe

    # installed Python 2.7.18
C:\Users\bmarr\AppData\Local\Python2.7\python.exe

    # Spyder python
    #  ==> Python 3.11.11 | packaged by conda-forge | (main, Dec  5 2024, 14:06:23) [MSC v.1942 64 bit (AMD64)]
    #  ==> IPython 8.32.0 -- An enhanced Interactive Python.
C:\Users\bmarr\AppData\Local\spyder-6\python.exe
C:\Users\bmarr\AppData\Local\spyder-6\envs\spyder-runtime\python.exe



C:\Users\bmarr\AppData\Local\Microsoft\WindowsApps\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\python.exe

# %%

'''
    search for pip
    '''
C:\>dir /b/s pip.exe

    # python 2.7 has pip
C:\Users\bmarr\AppData\Local\Python2.7\Scripts\pip.exe

    # spyderhas pip
C:\Users\bmarr\AppData\Local\spyder-6\envs\spyder-runtime\Scripts\pip.exe
C:\Users\bmarr\AppData\Local\spyder-6\Scripts\pip.exe

    # 

# %%

'''
    search for virtualenv
 '''
 
    
   # google-cloud-sdk bundled python has venv folder
C:\Users\bmarr\AppData\Local\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython\Lib\venv\scripts\nt\python.exe


    # spyder python has venv folder
C:\Users\bmarr\AppData\Local\spyder-6\envs\spyder-runtime\Lib\venv\scripts\nt\python.exe
C:\Users\bmarr\AppData\Local\spyder-6\Lib\venv\scripts\nt\python.exe


    # virtualenv has virtualenv.exe
    # find it
C:\> dir /b/s virtual.exe >> C:\Users\dassn\OneDrive\Escritorio\venv_exe_files.txt
File Not Found


# %%

'''
    Install virtualenv using pip in spyder
'''

    # install virtualenv
    # virtualenv.exe will likely now be found in your python installation directory 
    # under the Scripts subdirectory.


C:\Users\dassn\AppData\Local\spyder-6\Scripts> pip install virtualenv

Collecting virtualenv
  Downloading virtualenv-20.29.3-py3-none-any.whl.metadata (4.5 kB)
  ....
virtualenv in c:\users\bmarr\appdata\local\spyder-6\lib\site-packages (20.29.3)
  
      # verify installation and locate
C:\>dir /b/s virtualenv.exe
C:\Users\dassn\AppData\Local\spyder-6\Scripts\virtualenv.exe


# %%

'''
  install Python 2.7 just for me
'''
https://stackoverflow.com/questions/13596505/python-command-not-working-in-command-prompt
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

    #  in Windows search, Advanced System Settings to find env variables
      # Don't mess with PYTHONPATH environmental variable
      # DO NOT change python env to PYTHONPATH env variable
 C:\Users\bmarr\AppData\Local\Python2.7
 
 
 
    # Python3 is here as python.exe and/or python3
C:\Users\bmarr\AppData\Local\spyder-6>


 # install pyhton 2.7 Windows
Python 2.7.18 is the last release of Python 2.
https://www.python.org/downloads/release/python-2718/


    #Python 2 is here
C:\Python27\
    
  
  
 


# %%



=======   Google Preliminaries   ===========================

# %%

'''
Login to Google Cloud account (marron,bruce,mx@gmail,com)
Activate Cloud Shell 
Check account status and exit Cloud Shell
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
Install gcloud SDK (gcloud CLI) on home compu 

'''

    #Download installer .exe  OR Open Power Shell for cmd line install

https://cloud.google.com/sdk/docs/install
==> GoogleCloudSDKInstaller.exe

   # installer places SDK here
C:\Users\bmarr\AppData\Local\Google\Cloud SDK
 
     * CLI libraries
     * Bundled Python
     * Cloud Tools for PowerShell
     
     * accept all defaults on last page of installer
     * Google Cloud Version 513.0.0

    # 'bundled with Python 3" means that the scripts are in python3
    # 'run a supported version of Python' means having python installed
    
 By default, the Windows version of Google Cloud CLI comes bundled with 
 Python 3. To use Google Cloud CLI your operating system must be able to 
 run a supported version of Python.
 
 While Google Cloud CLI installs and manages Python 3 by default, you can use 
 an existing Python installation if necessary by unchecking the option
 to Install Bundled Python.
 
      
    # Once installed get a PowerShell terminal to sign in
> You must sign in to continue. Would you like to sign in (Y/n)?

    * asks for Google Cloud acct emai
    * phone verification (TFA)
    * Google Cloud wants access your Google acct
    
You are now authenticated with the gcloud CLI!
    https://cloud.google.com/sdk/auth_success
    
    # more info
    https://cloud.google.com/sdk/gcloud

# %%

> You are signed in as: [marron.bruce.mx@gmail.com].

> Pick cloud project to use:
 [1] my-project-uteca1
 [2] Enter a project ID
 [3] Create a new project
Please enter numeric choice or text value (must exactly match list item):
    
    
This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.


Some things to try next:
* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the CLI like arg files and output formatting
* Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.



    # ALL google-cloud-sdk files here
C:\Users\bmarr\AppData\Local\Google\Cloud SDK>


# %%
'''
Check for google-cloud-sdk updates
Revert google-cloud-sdk to previous version (if needed)
'''
https://stackoverflow.com/questions/71949010/google-cloud-sdk-python-was-not-found

C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud components update

All components are up to date.

    # To revert your CLI to the previously installed version:
C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud components update --version 505.0.0
  
  
  # helpful (about Python)
> gcloud topic startup 
 
> gcloud cheat-sheet


CLOUDSDK_PYTHON <== env variable
        #add new env variable for google cloud point to Spyder-6



  
  

# %%
 
 '''
    Obtain Application Default Credentials (ADC)
    (Only once; stored as .json file)
 '''


C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud auth application-default login
    * select Google acct
    * Sign in to Google Auth Library
Google Auth Library wants to access your Google Account

   # set the authentication account
   # if needed
C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud config set account `ACCOUNT`   #<== re-type 'ACCOUNT' w/ apostrophes!!



        # check for credentialed accounts
C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud auth list

      Credentialed Accounts
ACTIVE  ACCOUNT
*       marron.bruce.mx@gmail.com


'''
    ADC Credentials
'''
   # Initial get of ADC credentials 
   # will be stored locally as .json file
   # ADC authentication is thru google-cloud-sdk 
   # Browser sent to Google Auth Library; follow browser prompts
   # NOT setting up a Service Account; ADC stored locally
   # once have credentials will be used by any library that requests ADCs


C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud auth application-default set-quota-project phonic-skyline-452123-e2

Credentials saved to file: 
    [C:\Users\bmarr\AppData\Roaming\gcloud\application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).
Quota project "my-project-uteca1" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.


Quota project "my-project-uteca1" was added to ADC which can be used by 
Google client libraries for billing and quota.


    # ADC credentials Credentials saved to file: 
C:\Users\bmarr\AppData\Roaming\gcloud\application_default_credentials.json



# %%
#START HERE!!!
============== Workflow_gcloudAPI_StandardNMT_GeneralTranslation_WINDOWS_docs.py  ============

# %%

'''
Doing complete document translations thru API with the Standard NMT model
  Account and Project Configuration
  (Re-set every session)
'''

  # sign in and follow prompts for account and project config
  #  ==> follow prompts
  
C:\Users\bmarr\AppData\Local\Google\Cloud SDK> gcloud init

Welcome! This command will take you through the configuration of gcloud.....

Settings from your current configuration [default] are:
accessibility:
  screen_reader: 'False'
core:
  account: marron.bruce.mx@gmail.com
  disable_usage_reporting: 'False'
  project: my-project-uteca1

Pick configuration to use:
 [1] Re-initialize this configuration [default] with new settings
 [2] Create a new configuration
Please enter your numeric choice:


Select an account:
 [1] marron.bruce.mx@gmail.com
 [2] Sign in with a new Google Account
 [3] Skip this step
Please enter your numeric choice:



Pick cloud project to use:
 [1] my-project-uteca1
 [2] Enter a project ID
 [3] Create a new project
Please enter numeric choice or text value (must exactly match list item):
    

The Google Cloud CLI is configured and ready to use!


# %%
'''
    Create a virtual Python environment on local machine (home computer)
      ==> Install IPython
      ==> Install the SDK for Google language translation (google-cloud-translate)
      ( aka the Google Translation API client library)
      ==> spyder kernels
'''

 # Spyder ISSUES !! TO FIX!!
# installed spyder kernels separately
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda install spyder-kernels=3.0
    #check contents
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> dir /b/s venv-translate >> C:\Users\bmarr\Desktop\venv.txt
    # found python.exe but spyder won't accept this
C:\Users\bmarr\AppData\Local\spyder-6\Scripts\venv-translate\Scripts\python.exe





    # cd to the directory with virtualenv.exe
C:\Users\bmarr> cd C:\Users\dassn\AppData\Local\spyder-6\Scripts

 
     # create virtual env, 'venv-translate'
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> virtualenv venv-translate


    # activate
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> activate


    # activated !!
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts>



    # install ipython google-cloud-translate
    # NOT spyder-kernels==3.0.*
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts> pip install ipython google-cloud-translate


   #RUN ipython from terminal
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts>ipython

Python 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:27:10) [MSC v.1938 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.33.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:




# %%
'''
    Import modules
      ==> os
    Import methods (fxns)
      ==> google.cloud.translate_v3.services.translation_service.TranslationServiceAsyncClient.translate_text
      ==> google.cloud.translate_v3.services.translation_service.TranslationServiceClient
      ==> method "translate_v3" from google.cloud.translate (SDK)
'''

import os
#from google.cloud import translate
from google.cloud import translate_v3 as translate


# %%
'''
  Set Google API variables 
  Set Google credentials for billing and quots
'''
  # Google Cloud project used for translation work
PROJECT_ID = "phonic-skyline-452123-e2";
assert PROJECT_ID ;
project_id = PROJECT_ID


  # set ADC from Google as a Python env variable 
credential_path = "C:\\Users\\dassn\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# %%
'''
    Set name and path of doc to be translated
    Set target language (code) for translation
'''

     # document to be translated
     # path to the document
doc_to_translate = "01 Convocatoria CACON 0030 2025.pdf" ;
doc_dir = "C:\\Users\\dassn\\OneDrive\\Escritorio" ;
file_path = os.path.join(doc_dir, doc_to_translate)


    # target language for translation
target = "zh"



# %%
'''
    Define the Python translation fxn, "translate_document"
    Source:
https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_document
'''

    # NB indents REMOVED from All original code lines o/w "indent errors" IPython
    # NB path separators (forward slashes) must be DOUBLED (escape the fist slash )
    # NB Windows add a HIDDEN .pdf extension to pdf files!!
    # NB cut/paste the ENTIRE translation fxn into IPython
    
    
    # the translation fxn: single doc to single language
    
def translate_document(project_id: str,file_path: str,):   

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
    
    f = open('C:\\Users\\dassn\\OneDrive\\Escritorio\\gcTranslate_output.pdf', 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    print(f"Response: Detected Language Code - {response.document_translation.detected_language_code}")
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

      

 
    # To stop using the Python virtual environment
    # DEACTIVATE and rmdir 
    
    # If needed, initialize conda
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda init

 
     # DEACTIVATE
     # restart terminal to send deactivate command
     # conda deactivate 
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda deactivate 
    

    
   # DELETE virtual environment folder and all files
   #    ==>  /q disables Yes/No prompting
   #    ==> /s means delete the file(s) from all subdirectories.
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> rmdir /s /q venv-translate

    # check
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> dir /b/s venv-translate
    File Not Found


# [Workflow_gcloudAPI_StndNMT_GenTranslation_WINDOWS_docs]

