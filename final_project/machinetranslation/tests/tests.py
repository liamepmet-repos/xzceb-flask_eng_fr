'''
This module has the unit tests for module translator.py

METHODS:
TestEnglishToFrench
TestFrenchToEnglish
'''
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''this class has english to french test cases'''
    def test_for_null(self):
        '''test for null (None) english_to_french method'''
        self.assertIsNone(english_to_french(None),None)

    def test_translation(self):
        '''test for translation english_to_french method'''
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    '''this class has french to english test cases'''
    def test_for_null(self):
        '''test for null (None) french_to_english method'''
        self.assertIsNone(french_to_english(None),None)

    def test_translation(self):
        '''test for translation french_to_english method'''
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
