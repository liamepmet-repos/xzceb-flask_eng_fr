
'''
This module uses the IBM languageTranslatorv3 library to translate text from
English to French and French To English

METHODS:
english_to_french(string)
french_to_english(string)
'''

import os
import re
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# test API
#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    '''This method translates text from English to French'''
    try:
        en2fr = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        french_text = en2fr["translations"][0]["translation"]
        return french_text
    except Exception as error:
        error_str =  str(error)
        if re.search("text must be provided|'text' is empty",error_str):
            return None

def french_to_english(french_text):
    '''This method translates text from French to English'''
    try:
        fr2en = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        english_text = fr2en["translations"][0]["translation"]
        return english_text
    except Exception as error:
        error_str =  str(error)
        if re.search("text must be provided|'text' is empty",error_str):
            return None
