#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:35:19 2025

@author: bmarron
"""

# %%

'''
Using the Natural Language Tool Kit (ntlk)
[see installation in 'Install-Info_NLTK-package.txt']

'''

# %%

import nltk
nltk.download()

# %%

'''
Test Code

'''

from nltk.translate.bleu_score import sentence_bleu

# Define your desired weights (example: higher weight for bi-grams)
weights = (0.25, 0.25, 0, 0)  # Weights for uni-gram, bi-gram, tri-gram, and 4-gram

# Reference and predicted texts (same as before)
reference = [["the", "picture", "is", "clicked", "by", "me"],
             ["this", "picture", "was", "clicked", "by", "me"]]
predictions = ["the", "picture", "the", "picture", "by", "me"]

# Calculate BLEU score with weights
score = sentence_bleu(reference, predictions, weights=weights)
print(score)

# %%

#from nltk.translate.bleu_score import corpus_bleu

from nltk.tokenize import sent_tokenize

text = "NLTK is a great NLP toolkit. It makes processing text easy!"
sentences = sent_tokenize(text)
print(sentences)

# %%

import os
from nltk.tokenize import sent_tokenize, word_tokenize

    # Setup for output
OUTPUT_FILE = "tokenized_refs.txt"

doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Define reference texts
    # tokenize to sentences and then to words
reference_text_1 = "This is a long and complex reference text for evaluating the machine translation output. It contains multiple sentences and aims to provide a comprehensive example."
reference_text_2 = "Another reference text that is also long and provides a different perspective on the same topic. This helps in capturing more nuances."

references = [
        [word_tokenize(sent) for sent in reference_text_1.split('. ') if sent],
        [word_tokenize(sent) for sent in reference_text_2.split('. ') if sent]
    ]

    # If the list contains elements of other data types 
    # you need to convert them to strings before joining
    # use map(str, <list_name>)
refs_string = ",".join(map(str, references))

with open(output_filepath, "w", encoding="utf-8") as f:
     f.write(refs_string)

#print(references)

# %%


import os
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize, word_tokenize

    # Setup for output
OUTPUT_FILE = "tokenized_refs.txt"

doc_to_print = OUTPUT_FILE;
doc_dir = "/home/bmarron/Desktop" ;
output_filepath = os.path.join(doc_dir, doc_to_print)

    # Define reference texts 
 
reference_text_1 = "SEXTO. En principio será motivo de análisis el motivo de inconformidad que se refiere a la existencia de violación a las reglas del procedimiento laboral, porque de resultar fundado haría innecesario el estudio de los restantes. El apoderado legal de las quejosas señala lo siguiente: a) Que en la audiencia trifásica celebrada el veintidós de mayo de dos mil dos, en el expediente número 47.2001, se ofreció, entre otras, la inspección ocular que debería realizarse en el domicilio de la demandada sobre las listas de raya, nóminas de personal, recibos o comprobantes de sueldos o salarios, tarjetas de control de asistencia y demás documentación que acostumbre llevar o utilice para el manejo de su personal, por el periodo comprendido del veintidós de noviembre de dos mil al veintidós de noviembre de dos mil uno, con la finalidad de acreditar que los nombres de los actores aparecen en dichos documentos como trabajadores de la demandada. Petición que la Junta responsable acordó favorable en acuerdo de diecinueve de agosto de ese año, apercibiendo a la parte demandada con fundamento en el artículo 828 de la Ley Federal del Trabajo, que de no exhibir la documentación requerida se tendrían por presuntivamente ciertos los hechos que la parte actora pretende probar."
#reference_text_2 = "Another reference text that is also long and provides a different perspective on the same topic. This helps in capturing more nuances."

candidate_text = "SIXTH. In principle, the reason for disagreement that refers to the existence of a violation of the rules of labor procedure will be a reason for analysis, because if it is founded it would make the study of the remaining ones unnecessary. The legal representative of the complainants points out the following: a) That in the three-phase hearing held on May 22, 2002, in file number 47.2001, it was offered, among others, the ocular inspection that should be carried out at the defendant's domicile on the payroll lists, personnel payrolls, receipts or vouchers for salaries or wages, attendance control cards and other documentation that it usually keeps or uses for the management of its personnel, for the period from November 22, 2000 to November 22, 2001, with the purpose of proving that the names of the actors appear in said documents as workers of the defendant. Request that the responsible Board agreed to favorably in an agreement of August 19 of that year, warning the defendant based on article 828 of the Federal Labor Law, that if the required documentation is not exhibited, the facts that the plaintiff intends to prove would be presumed to be true."

   # tokenize to sentences and then to words
references = [
        [word_tokenize(sent) for sent in reference_text_1.split('. ') if sent],
#        [word_tokenize(sent) for sent in reference_text_2.split('. ') if sent]
    ]

candidate = [word_tokenize(sent) for sent in candidate_text.split('. ') if sent]

weights=(.75, 0.25, 0, 0)

bleu_score = corpus_bleu(references, candidate, weights)
 
print(bleu_score)


# %%

