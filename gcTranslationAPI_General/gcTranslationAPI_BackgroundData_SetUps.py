#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:54:30 2024

@author: bmarron
"""



    
# %%

'''
     On Google Authentication...
'''
    #  in Google Cloud Console (w/o IPython) Neural Machine Translation (NMT)

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
T     On Google Account and Project Configuration
'''
    #  in Google Cloud Console (w/o IPython)

$ gcloud config set account 'ACCOUNT'     # <== retype w/ single quotes ''

$ gcloud config list project
 

# %%

'''
    On Google Cloud Translation API
'''

    #  in Google Cloud Console (w/o IPython)

$ gcloud services enable translate.googleapis.com


# %%

'''
   On Set the PROJECT_ID environment variable (to be used in your application)
'''
https://stackoverflow.com/questions/35599414/get-the-default-gcp-project-id-with-a-cloud-sdk-cli-one-liner

#  in Google Cloud Console (w/o IPython)


$ export PROJECT_ID=$(gcloud config get-value core/project)
    #Your active configuration is: [cloudshell-22175]
$ echo "PROJECT_ID: $PROJECT_ID"
    #PROJECT_ID: my-project-uteca1
    


# %%

'''
   On creating a virtual Python environment on your home computer
    Installing IPython and the Translation API client library (an SDK)
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
    On calling IPython in Cloud Shell
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
    On initial attempts at using Spyder for Google Cloud APIs
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

List of methods/fxn in Google API

https://stackoverflow.com/questions/69964961/how-can-i-get-a-list-of-google-cloud-functions-using-google-python-client-for-cl

from google.cloud.functions_v1.services.cloud_functions_service import CloudFunctionsServiceClient
from google.cloud.functions_v1.types import ListFunctionsRequest
list_functions_request = ListFunctionsRequest(parent=f"projects/{project}/locations/{region}")
await CloudFunctionsServiceClient().list_functions(list_functions_request)



# %%

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables. 
If you want a list of those, they are defined in the standard module 
builtins:

import builtins

dir(builtins)



# %%

'''
     Exit Python
     Close virtual environment
    
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

  *args ==>  allows you to pass a varying number of positional arguments.
  Extended sequence assignments use * (p. 74, 82 in Pocket Reference)
  
  The unpacking operator (*) creates a tuple not a list: A tuple is similar to a list in 
  that they both support slicing and iteration. However, tuples are very different in at least 
  one aspect: lists are mutable, while tuples are not. 

