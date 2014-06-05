from unittest import TestCase
from docclass import Classifier

__author__ = 'maria'


class TestGetwords(TestCase):

    def testClassifier(self):
        c = Classifier()
        dict = c.getfeatures("Hello World world world ,       hello has cats and vervyveryveryveryveryverylongword")
        self.assertIsNotNone(dict)
        self.assertIsNotNone(dict["hello"])
        self.assertEqual(dict["hello"], 1)
        self.assertFalse(dict.has_key("has"))
        self.assertFalse(dict.has_key("vervyveryveryveryveryverylongword"))