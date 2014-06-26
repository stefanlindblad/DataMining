from unittest import TestCase
import numpy as np
from newsfeatures import cost

class TestFunctions(TestCase):

    def test_cost(self):
        A = np.arange(9).reshape((3,3))
        B = np.arange(1,10).reshape((3,3))

        self.assertEqual(cost(A,B), 9, 'cost function does not work.')