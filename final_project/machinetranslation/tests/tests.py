from ibm_watson import ApiException
from translator import french_to_english, english_to_french
import unittest

class TestEnglish2French(unittest.TestCase):
    def test1(self):
        self.assertRaises(ApiException, english_to_french, "")
        self.assertNotEqual(english_to_french("None"), '')
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrench2English(unittest.TestCase):
    def test1(self):
        self.assertRaises(ApiException, french_to_english, "")
        self.assertNotEqual(french_to_english("None"), '')
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()