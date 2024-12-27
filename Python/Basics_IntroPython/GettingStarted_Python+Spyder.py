# %%
# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""
import sys
print(sys.version)

'''
In [1]: %runcell -i 1 /home/bmarron/.config/spyder-py3/temp.py
3.11.10 | packaged by conda-forge | (main, Oct 16 2024, 01:27:36) [GCC 13.3.0]
# %%
'''

# %%

# new cells  (Ctrl+2)

# %%

''' 
https://www.w3schools.com/python

https://www.devopsschool.com/blog/python-tutorials-difference-between-list-array-tuple-set-dict/

'''

# %%

'''
Note: The first item has index 0.

This answer will sum up almost all the queries about when to use List and Array:

    The main difference between these two data types is the operations you 
    can perform on them. For example, you can divide an array by 3 and it 
    will divide each element of array by 3. Same can not be done with the list.

    The list is the part of python's syntax so it doesn't need to be declared 
    whereas you have to declare the array before using it.

    You can store values of different data-types in a list (heterogeneous), 
    whereas in Array you can only store values of only the same data-type 
    (homogeneous).

    Arrays being rich in functionalities and fast, it is widely used for 
    arithmetic operations and for storing a large amount of data - compared 
    to list.

    Arrays take less memory compared to lists.

'''

# %%

'''
Most things in Python are objects. But what is an object?

Every constant, variable, or function in Python is actually a object with a 
type and associated attributes and methods. An attribute a property of the 
object that you get or set by giving the <object_name> + dot + <attribute_name>, 
for example img.shape. A method is a function that the object provides, 
for example img.argmax(axis=0) or img.min().

Use tab completion in IPython to inspect objects and start to understand 
attributes and methods.ie  LIST_NAME.<TAB>
'''

a = [3, 1, 2, 1]
print(a)
a.reverse()
print(a)

# %%

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 
# %%

'''
USE THIS!!
https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0


https://cloud.google.com/translate/docs/reference/rest#service:-translate.googleapis.com
Service: translate.googleapis.com
To call this service, we recommend that you use the Google-provided client libraries. If your application needs to use your own libraries to call this service, use the following information when you make the API requests.


https://cloud.google.com/translate/?hl=en
Cloud Translation API (Google)
Cloud Translation API uses Google's neural machine translation technology to let 
you dynamically translate text through the API using a Google pre-trained, custom model, or a 
translation specialized large language model (LLMs). 

It comes in Basic and Advanced editions. Both provide fast and dynamic translation, but Advanced 
offers customization features, such as domain-specific translation, formatted document translation, 
and batch translation.

The first 500,000 characters sent to the API to process (Basic and Advanced combined) per month are 
free (not applicable to LLMs).


Model selection
For advanced translations, you're not limited to a one-size-fits-all solution, ensuring the highest 
quality and accuracy for your specific content. You can choose from the following models, based on 
your needs:

Neural Machine Translation (NMT) for general text in everyday use cases like website content or news 
articles.

Translation Large Language Model (LLM) for conversational text like messages or social media posts. 
You can use "Adaptive" mode to fine-tune translations based on your own examples for an even closer 
match to your unique style.


https://cloud.google.com/apis/docs/cloud-client-libraries
Working with Cloud Client Libraries
Cloud Client Libraries by language
The following table provides links to get you started with Cloud Client Libraries in supported languages. The GitHub Repo page for each language lists the Cloud Platform services/APIs that are supported by that language's Cloud Client Library. The page also has installation instructions for a single client library that provides an interface to the APIs.

Python 	
    GitHub Repo
    Library Reference 
        Cloud Translation 	google-cloud-translate


# %%


https://console.cloud.google.com/
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


Project name
    My Project-UTECA1
Project number
    735387290281
Project ID
    my-project-uteca1 


 From the Cloud Console, click Activate Cloud Shell 

--- a command line interface
Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to my-project-uteca1.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
marron_bruce_mx@cloudshell:~ (my-project-uteca1)$ 



'''
# %%

# in Google Cloud

gcloud auth list
    #Cloud Shell needs permission to use your credentials for the gcloud CLI command.
    #Click Authorize to grant permission to this and future calls. 
    #--- need to activate Free Trial to authenticate account

gcloud auth list
    #ACTIVE: *
    #ACCOUNT: marron.bruce.mx@gmail.com


gcloud config set account 'ACCOUNT' <== retype single quotes ''
    #Updated property [core/account].

gcloud config list project
    #[core]
    #project = my-project-uteca1
    #Your active configuration is: [cloudshell-9018]

gcloud services enable translate.googleapis.com
    #ERROR: (gcloud.services.enable) Your current active account [ACCOUNT] does not have any valid credentials
    Please run:
        $ gcloud auth login
        to obtain new credentials.

--- credential
$ 4/0AanRRruInSQf9hOK5NOIHwwjSeZ9OuF97N2wGAlFfTFZHLoMLCvFvfnehOq5K4_OpGxrSw
    #You are now logged in as [marron.bruce.mx@gmail.com].
   # Your current project is [my-project-uteca1].


gcloud services enable translate.googleapis.com
    #Operation "operations/acat.p2-735387290281-9ce6663f-72ab-40a2-84f7-5c5802490b1a" finished successfully.
    # Now, you can use the Translation API!
    
export PROJECT_ID=$(gcloud config get-value core/project)
    #Your active configuration is: [cloudshell-22175]
echo "PROJECT_ID: $PROJECT_ID"
    #PROJECT_ID: my-project-uteca1
    
--- NO GO ==> dont use a virtual env; create new folder (GoogleAPI) in Anaconda3 directory
bmarron@bmarron-HP-Laptop-15t-dy100:~/anaconda3/GoogleAPI$ pip install google-cloud-translate
    #Successfully installed cachetools-5.5.0 google-api-core-2.24.0 google-auth-2.37.0 google-cloud-core-2.4.1 google-cloud-translate-3.19.0 googleapis-common-protos-1.66.0 grpc-google-iam-v1-0.13.1 grpcio-1.68.1 grpcio-status-1.68.1 proto-plus-1.25.0 protobuf-5.29.2 pyasn1-0.6.1 pyasn1-modules-0.4.1 rsa-4.9
    # The following NEW packages will be installed:
  libexpat1-dev{a} libjs-sphinxdoc{a} libjs-underscore{a} libpython3-dev{a} 
  libpython3.10-dev{a} python3-dev{a} python3-distutils{a} 
  python3-lib2to3{a} python3-pip python3-setuptools{a} python3-wheel{a} 
  python3.10-dev{a} zlib1g-dev{a} 

https://cloud.google.com/python/docs/getting-started
https://cloud.google.com/python/docs/setup
https://cloud.google.com/python/docs/reference Python Cloud Client Libraries
https://cloud.google.com/apis/docs/client-libraries-explained Cloud Client Libraries
https://developers.google.com/api-client-library/

https://developers.google.com/apis-explorer/
https://cloud.google.com/translate/docs/setup
https://cloud.google.com/translate/docs/reference/rest


# %%
    # actually running code to interface with Google API

from os import environ

from google.cloud import translate


PROJECT_ID = environ.get("PROJECT_ID", "")
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"

# %%

def print_supported_languages(display_language_code: str):
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
awa       Awadhi
ay        Aymara
az        Azerbaijani
ban       Balinese
bm        Bambara
ba        Bashkir
eu        Basque
btx       Batak Karo
bts       Batak Simalungun
bbc       Batak Toba
be        Belarusian
bem       Bemba
bn        Bengali
bew       Betawi
bho       Bhojpuri
bik       Bikol
bs        Bosnian
br        Breton
bg        Bulgarian
bua       Buryat
yue       Cantonese
ca        Catalan
ceb       Cebuano
ny        Chichewa
zh        Chinese (Simplified)
zh-CN     Chinese (Simplified)
zh-TW     Chinese (Traditional)
cv        Chuvash
co        Corsican
crh       Crimean Tatar
hr        Croatian
cs        Czech
da        Danish
dv        Dhivehi
din       Dinka
doi       Dogri
dov       Dombe
nl        Dutch
dz        Dzongkha
en        English
eo        Esperanto
et        Estonian
ee        Ewe
fj        Fijian
tl        Filipino
fil       Filipino
fi        Finnish
fr        French
fy        Frisian
ff        Fulani
gaa       Ga
gl        Galician
ka        Georgian
de        German
el        Greek
gn        Guarani
gu        Gujarati
ht        Haitian Creole
cnh       Hakha Chin
ha        Hausa
haw       Hawaiian
iw        Hebrew
he        Hebrew
hil       Hiligaynon
hi        Hindi
hmn       Hmong
hu        Hungarian
hrx       Hunsrik
is        Icelandic
ig        Igbo
ilo       Ilocano
id        Indonesian
ga        Irish
it        Italian
ja        Japanese
jw        Javanese
jv        Javanese
kn        Kannada
pam       Kapampangan
kk        Kazakh
km        Khmer
cgg       Kiga
rw        Kinyarwanda
ktu       Kituba
gom       Konkani
ko        Korean
kri       Krio
ku        Kurdish (Kurmanji)
ckb       Kurdish (Sorani)
ky        Kyrgyz
lo        Lao
ltg       Latgalian
la        Latin
lv        Latvian
lij       Ligurian
li        Limburgish
ln        Lingala
lt        Lithuanian
lmo       Lombard
lg        Luganda
luo       Luo
lb        Luxembourgish
mk        Macedonian
mai       Maithili
mak       Makassar
mg        Malagasy
ms        Malay
ms-Arab   Malay (Jawi)
ml        Malayalam
mt        Maltese
mi        Maori
mr        Marathi
chm       Meadow Mari
mni-Mtei  Meiteilon (Manipuri)
min       Minang
lus       Mizo
mn        Mongolian
my        Myanmar (Burmese)
nr        Ndebele (South)
new       Nepalbhasa (Newari)
ne        Nepali
no        Norwegian
nus       Nuer
oc        Occitan
or        Odia (Oriya)
om        Oromo
pag       Pangasinan
pap       Papiamento
ps        Pashto
fa        Persian
pl        Polish
pt        Portuguese (Brazil)
pa        Punjabi (Gurmukhi)
pa-Arab   Punjabi (Shahmukhi)
qu        Quechua
rom       Romani
ro        Romanian
rn        Rundi
ru        Russian
sm        Samoan
sg        Sango
sa        Sanskrit
gd        Scots Gaelic
nso       Sepedi
sr        Serbian
st        Sesotho
crs       Seychellois Creole
shn       Shan
sn        Shona
scn       Sicilian
szl       Silesian
sd        Sindhi
si        Sinhala
sk        Slovak
sl        Slovenian
so        Somali
es        Spanish
su        Sundanese
sw        Swahili
ss        Swati
sv        Swedish
tg        Tajik
ta        Tamil
tt        Tatar
te        Telugu
tet       Tetum
th        Thai
ti        Tigrinya
ts        Tsonga
tn        Tswana
tr        Turkish
tk        Turkmen
ak        Twi
uk        Ukrainian
ur        Urdu
ug        Uyghur
uz        Uzbek
vi        Vietnamese
cy        Welsh
xh        Xhosa
yi        Yiddish
yo        Yoruba
yua       Yucatec Maya
zu        Zulu

# %%

def translate_text(text: str, target_language_code: str) -> translate.Translation:
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        parent=PARENT,
        contents=[text],
        target_language_code=target_language_code,
    )

    return response.translations[0]

# %%

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

# %%

    # https://cloud.google.com/translate/docs/advanced/translating-text-v3#translate_v3_translate_text-python
 
    Learn more

    # Cloud Translation documentation: https://cloud.google.com/translate/docs
    # Python on Google Cloud: https://cloud.google.com/python
    # Cloud Client Libraries for Python: https://github.com/googleapis/google-cloud-python

 
    # https://docs.spyder-ide.org/5/faq.html#using-packages-installer
    

# %%

    Clean up

To clean up your development environment, from Cloud Shell:

    If you're still in your IPython session, go back to the shell: exit
    Stop using the Python virtual environment: deactivate
    Delete your virtual environment folder: cd ~ ; rm -rf ./venv-translate

To delete your Google Cloud project, from Cloud Shell:

    Retrieve your current project ID: PROJECT_ID=$(gcloud config get-value core/project)
    Make sure this is the project you want to delete: echo $PROJECT_ID
    Delete the project: gcloud projects delete $PROJECT_ID

# %%



