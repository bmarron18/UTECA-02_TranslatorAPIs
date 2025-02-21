#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 2025
@author: bmarron

source: https://cloud.google.com/translate/docs/advanced/adaptive-translation
"""

# %%

# NEEDS WORK!!

# %%

def adaptive_mt_translate():
  # Create a client
  client = translate.TranslationServiceClient()
  # Initialize the request
  request = translate.AdaptiveMtTranslateRequest(
    parent="projects/PROJECT_ID/locations/LOCATION",
    reference_sentence_config=[
      "reference_sentence_pair_lists": [
        "reference_sentence_pairs": {
          "source_sentence": 'REFERENCE_SOURCE_1_1'
          "target_sentence": 'REFERENCE_TARGET_1_1'
        },
        "reference_sentence_pairs": {
          "source_sentence": 'REFERENCE_SOURCE_1_2'
          "target_sentence": 'REFERENCE_TARGET_1_2'
        }
      ],
      "source_language_code": 'SOURCE_LANGUAGE'
      "target_language_code": 'TARGET_LANGUAGE'
    ],
    content=["SOURCE_TEXT"]
  )
  # Make the request
  response = client.adaptive_mt_translate(request)
  # Handle the response
  print(response)




