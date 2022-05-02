import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null(self):
        self.assertIsNone(englishToFrench(""),None)

    def test_translation(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null(self):
        self.assertIsNone(frenchToEnglish(""),None)

    def test_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()