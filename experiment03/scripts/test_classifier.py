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

    def testTrain(self):
        c = Classifier(getwords)
        item = "Hello hello world, my name is Python."
        cat = "Good"
        c.train(item, cat)
        self.assertEqual(c.catcount("Good"), 1)
        self.assertEqual(c.fcount("hello", "Good"), 1)
        self.assertFalse(c.fc.has_key("my"))

    def testFProb(self):
        c = Classifier(getwords)
        c.incc("Good")
        c.incf("hello", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        self.assertEqual(c.fprob("world", "Good"), 2.0/3.0)

    def testWeightedProb(self):
        c = Classifier(getwords)
        c.incc("Good")
        c.incf("hello", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        c.incc("Bad")
        c.incf("world", "Bad")
        self.assertEqual(c.weightedprob("world", "Good"), 5.0/8.0)
        self.assertEqual(c.weightedprob("wurst", "Good"), 0.5)

    def testProb(self):
        c = Classifier(getwords)

        # training
        c.incc("Good")
        c.incf("hello", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        c.incc("Good")
        c.incf("world", "Good")
        c.incc("Bad")
        c.incf("world", "Bad")

        # classify new document
        item = "world world wurst Wurst wurst world"

        self.assertEqual(c.prob(item, "Good"), 0.234375)

    def testClassifier(self):
        c = Classifier(getwords)
        c.train("nobody owns the water", "Good")
        c.train("the quick rabbit jumps fences", "Good")
        c.train("buy pharmaceuticals now", "Bad")
        c.train("make quick money at the online casino", "Bad")
        c.train("the quick brown fox jumps", "Good")
        c.train("next meeting is at night", "Good")
        c.train("meeting with your superstar", "Bad")
        c.train("money like water", "Bad")

        # added quick to the test string, because with 'money jumps' Good and Bad got the same value.
        self.assertEqual(c.classify("the money jumps quick"), "Good")







