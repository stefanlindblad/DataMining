from unittest import TestCase
from docclass import Classifier
from docclass import getwords


class TestClassifier(TestCase):

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

        goodProb = c.prob("the money jumps", "Good")
        badProb = c.prob("the money jumps", "Bad")

        print c.classify("the money jumps")




