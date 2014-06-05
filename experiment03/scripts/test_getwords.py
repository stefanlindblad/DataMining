from unittest import TestCase
from docclass import Classifier
from docclass import getwords

__author__ = 'maria'


class TestGetwords(TestCase):

    def testGetFeatures(self):
        c = Classifier(getwords)
        dict = c.getfeatures("Hello World world world ,       hello has cats and vervyveryveryveryveryverylongword")
        self.assertIsNotNone(dict)
        self.assertIsNotNone(dict["hello"])
        self.assertEqual(dict["hello"], 1)
        self.assertFalse(dict.has_key("has"))
        self.assertFalse(dict.has_key("vervyveryveryveryveryverylongword"))

    def testIncF(self):
        c = Classifier(getwords)
        c.incf("hello", "Good")
        self.assertEqual(c.fc["hello"]["Good"], 1)
        c.incf("hello", "Good")
        self.assertEqual(c.fc["hello"]["Good"], 2)
        c.incf("hello", "Bad")
        self.assertEqual(c.fc["hello"]["Bad"], 1)

    def testIncC(self):
        c = Classifier(getwords)
        c.incc("Bad")
        self.assertEqual(c.cc["Bad"], 1)
        c.incc("Bad")
        self.assertEqual(c.cc["Bad"], 2)
        c.incc("Good")
        self.assertEqual(c.cc["Good"], 1)

    def testFCount(self):
        c = Classifier(getwords)
        c.incf("hello", "Good")
        c.incf("hello", "Good")
        c.incf("hello", "Bad")
        self.assertEqual(c.fcount("hello", "Good"), 2)
        self.assertEqual(c.fcount("hello", "Bad"), 1)
        self.assertEqual(c.fcount("wurst", "Bad"), 0)

    def testCatCount(self):
        c = Classifier(getwords)
        c.incc("Bad")
        c.incc("Bad")
        c.incc("Good")
        self.assertEqual(c.catcount("Good"), 1)
        self.assertEqual(c.catcount("Bad"), 2)

    def testTotalCount(self):
        c = Classifier(getwords)
        c.incc("Bad")
        c.incc("Bad")
        c.incc("Good")
        self.assertEqual(c.totalcount(), 3)
