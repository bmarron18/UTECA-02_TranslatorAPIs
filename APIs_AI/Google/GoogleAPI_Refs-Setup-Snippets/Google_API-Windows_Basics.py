#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:54:30 2024
Revised: 26 Sept 2025

@author: bmarron
"""


# %%

=====   [Command Line Operations in Windows] ===================


# %%

'''
Open/Close command line terminals in Windows
'''

* open a new terminal in Windows as an Adminstrator
    # Click the Start menu and type "cmd" in the search bar
    # find the Command Prompt (system)
    # select "run as administrator"

C:\windows\system32> 


* open a new terminal in Windows as a user
    # Click the Start menu and type "cmd" in the search bar
    # find the Command Prompt (system)
    # select "open"

C:\Users\bmarr> 



* open a terminal in a specific folder on Windows 
    # navigate to the desired folder in File Explorer
    # hold down the Shift key + right-click within the folder
    # select "Open in terminal" from the context menu. 
    
    
* close a terminal
    # type "exit" and hit Return
 
 # %%
 
 '''
 List/Change locations in the Windows filesystem
 
     cd == change directory
     /s == Displays all files and all subdirectories
     /b == bare format (no heading information or summary)
     /o == List by files in sorted order.
     :gn ==  g sorts by folders and then files
             n puts those files in alphabetical order
     >> == send output somewhere besides the terminal 
     files.txt == a new text file created as needed
     cd .. == go back one step in the filesytem
     

 
 '''
 
 * list files and directories at your current locations (general)
     # type "dir"
 
 C:\Users\bmarr> dir
 
 
 
 * list files and directories at your current locations (organized)
     # type "dir /s/b/o:gn"
     # send output to a text file on your desktop

C:\Users\bmarr> dir /s/b/o:gn >> C:\Users\bmarr\Desktop\files.txt



* change from current directory to the top of the filesystem (root directory)
    # type "cd/" 
    
C:\windows\system32> cd/
C:\>


* change from current directory to your home directory
    # type "cd %homedrive%%homepath%"
    # type "cd C:\Users\<your user name>"
    
C:\windows\system32> cd %homedrive%%homepath%
C:\Users\bmarr>

C:\windows\system32> cd C:\Users\bmarr\
C:\Users\bmarr>

 
 
 * go back one step (up) in the file system
     # type "cd .."
     
C:\Users\bmarr> cd ..
C:\Users



# %%

'''
    Search Windows filesystem
    
    *   == a wildcard symbol
    a  == specific attributes
        d  == directories only
        -d  == exclude directories; only files
        r  == Read-only files
        h  == hidden files
        s  == system files
        -   == NOT
  
'''
* References
    https://stackoverflow.com/questions/8066679/how-to-do-a-simple-file-search-in-cmd


* searches in current directory and sub-directories for a specific name
  (name of file OR directory)
    # type "dir /b/s *<name>*"

C:\Users\bmarr\Desktop> dir /b/s *Linux*
OUTPUT: C:\Users\bmarr\Desktop\general_Linux.txt


* searches either files OR directories for a specific name
    # /a-d excludes (attribute) directories; search only files
    # /ad  include (attribute) directories; search only directories

C:\Users\bmarr> dir /a-d /b/s *spyder*  >> C:\Users\bmarr\Desktop\spyder.txt
C:\Users\bmarr> dir /ad /b *spyder*  >> C:\Users\bmarr\Desktop\spyder2.txt



# %%

'''
    Search ALL Windows dorectories for Pyhton
'''
C:\Users\bmarr\> cd\
C:\> 

C:\> dir /b/s *python* >> C:\Users\bmarr\Desktop\python.txt

# %%

'''
    Search C:\ for pyhton.exe
'''
C:\Users\bmarr\> cd\
C:\> 

C:\> dir /b/s python.exe >> C:\Users\bmarr\Desktop\python_exe_files.txt


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
C:\> dir /b/s virtual.exe >> C:\Users\bmarr\Desktop\venv_exe_files.txt
File Not Found

# %%
'''
Install Notepad++
'''

C:\Program Files\Notepad++

# %%
'''
    install virtualenv with _conda in spyder?
'''
    # NO GO
C:\Users\bmarr\AppData\Local\spyder-6>_conda install virtualenv

NoBaseEnvironmentError: This conda installation has no default base environment. Use
'conda create' to create new environments and 'conda activate' to
activate environments.

# %%

'''
    Install virtualenv using pip in spyder
'''

    # install virtualenv
    # virtualenv.exe will likely now be found in your python installation directory 
    # under the Scripts subdirectory.


C:\Users\bmarr\AppData\Local\spyder-6\Scripts> pip install virtualenv

Collecting virtualenv
  Downloading virtualenv-20.29.3-py3-none-any.whl.metadata (4.5 kB)
  ....
virtualenv in c:\users\bmarr\appdata\local\spyder-6\lib\site-packages (20.29.3)
  
      # verify installation and locate
C:\>dir /b/s virtualenv.exe
C:\Users\bmarr\AppData\Local\spyder-6\Scripts\virtualenv.exe


   

# %%
'''
    CREATE virtual env in Windows
    ACTIVTE
    DELETE
'''

https://stackoverflow.com/questions/35950740/virtualenv-is-not-recognized-as-an-internal-or-external-command-operable-prog
https://stackoverflow.com/questions/46896093/how-to-activate-virtual-environment-from-windows-10-command-prompt
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html


    # CREATE a virtual environment
     # virtualenv is installed correctly
     # create virtual env, 'venv-translate'
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> virtualenv venv-translate


    # ACTIVATE the virtual environment
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> activate

    # activated !!
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts>

      # venv-translate directory exists? YES!!!
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> dir /b/s venv-translate 



    # To stop using the Python virtual environment
    # DEACTIVATE and rmdir 
    
    # First initialize conda
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda init
 ==> For changes to take effect, close and re-open your current shell
 
 
     # DEACTIVATE
     # restart terminal to send deactivate command
     # conda deactivate 
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda deactivate 
    

    
   # DELETE virtual environment folder and all files
   #    ==>  /q disables Yes/No prompting
   #    ==> /s means delete the file(s) from all subdirectories.
 C:\Users\bmarr\AppData\Local\spyder-6\Scripts> rmdir /s /q venv-translate

    # check
C:\Users\bmarr\AppData\Local\spyder-6\Scripts>dir /b/s venv-translate
File Not Found


   
   
    
# %%
'''
    Create a virtual Python environment on local machine (home computer)
      ==> Install IPython
      ==> Install the SDK for Google language translation (google-cloud-translate)
      ( aka the Google Translation API client library)
      ==> spyder kernels
'''
    
    # cd to directory with virtualenv.exe
C:\Users\bmarr> cd C:\Users\bmarr\AppData\Local\spyder-6\Scripts

 
     # create virtual env, 'venv-translate'
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> virtualenv venv-translate


    # activate
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> activate


    # activated !!
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts>



    # install ipython google-cloud-translate
    # NOT spyder-kernels==3.0.*
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts> pip install ipython spyder-kernels google-cloud-translate


    # installed spyder kernels separately
[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts> conda install spyder-kernels=3.0


    #check contents
C:\Users\bmarr\AppData\Local\spyder-6\Scripts> dir /b/s venv-translate >> C:\Users\bmarr\Desktop\venv.txt


    # found python.exe but spyder won't accept this
C:\Users\bmarr\AppData\Local\spyder-6\Scripts\venv-translate\Scripts\python.exe


    #RUN ipython from terminal

[spyder](base) C:\Users\bmarr\AppData\Local\spyder-6\Scripts>ipython

Python 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:27:10) [MSC v.1938 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.33.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:







# %%

