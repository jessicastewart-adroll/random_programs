"""Removing un-needed tests.

Tests converter functions' logic (conditional paths) and operators.
"""

import unittest
from roman_calc import Roman

class TestIntOperator(unittest.TestCase):
    def testSingleDigit(self):
        self.assertEqual(int(Roman("I")), 1)

    def testSuccessiveGreaterThan(self):
        self.assertEqual(int(Roman("VI")), 6)

    def testSuccessiveLessThan(self):
        self.assertEqual(int(Roman("IV")), 4)

class TestToRoman(unittest.TestCase):
    def testOnesOnly(self):
        self.assertEqual(Roman("I").to_roman(1), Roman("I"))

    def testThousandsOnly(self):
        self.assertEqual(Roman("MCMIX").to_roman(3000), Roman("MMM"))

    def testSkipTensHundreds(self):
        self.assertEqual(Roman("MCMIX").to_roman(3005), Roman("MMMV"))

    def testAll(self):
        self.assertEqual(Roman("MCMIX").to_roman(1959), Roman("MCMLIX"))

class TestOperators(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(Roman("III")+Roman("II"), Roman("V"))

    def testSubtraction(self):
        self.assertEqual(Roman("III")-Roman("II"), Roman("I"))

    def testMultiplication(self):
        self.assertEqual(Roman("III")*Roman("II"), Roman("VI"))

    def testEqualityTrue(self):
        self.assertTrue(Roman("I")==Roman("I"))

    def testEqualityFalse(self):
        self.assertFalse(Roman("I")==Roman("II"))

    def testInequalityTrue(self):
        self.assertTrue(Roman("I")!=Roman("II"))

    def testInequalityFalse(self):
        self.assertFalse(Roman("I")!=Roman("I"))

if __name__ == '__main__':
    unittest.main()
