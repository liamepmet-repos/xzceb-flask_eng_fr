import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import asyncio

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


def englishToFrench(englishText):
    en2fr = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = en2fr["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    fr2en = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = fr2en["translations"][0]["translation"]
    return englishText


print(englishToFrench("good morning"))
print(frenchToEnglish("Je ne parle pas français"))