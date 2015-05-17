import unittest
from roman_calc import Roman

class TestConvertToInt(unittest.TestCase):
	def testOnes(self):
		self.assertEqual(Roman("I").convert_to_int("I"), 1)

	def testTens(self):
		self.assertEqual(Roman("XLIV").convert_to_int("XLIV"), 44)

	def testHundreds(self):
		self.assertEqual(Roman("CCLIII").convert_to_int("CCLIII"), 253)

	def testThousands(self):
		self.assertEqual(Roman("MCMIX").convert_to_int("MCMIX"), 1909)

class TestConvertToRoman(unittest.TestCase):
	def testOnes(self):
		self.assertEqual(Roman("I").convert_to_roman(1), "I")

	def testTens(self):
		self.assertEqual(Roman("XLIV").convert_to_roman(44), "XLIV")

	def testHundreds(self):
		self.assertEqual(Roman("CCLIII").convert_to_roman(253), "CCLIII")

	def testThousands(self):
		self.assertEqual(Roman("MCMIX").convert_to_roman(1909), "MCMIX")

class TestRomanAttr(unittest.TestCase):
	def testRomanValue(self):
		self.assertEqual(Roman("I").roman, "I")

	def testIntValue(self):
		self.assertEqual(Roman("I").romans_int, 1)

class TestOperators(unittest.TestCase):
	def testAddition(self):
		self.assertEqual(Roman("III")+Roman("II"), "V")

	def testSubtraction(self):	
		self.assertEqual(Roman("III")-Roman("II"), "I")

	def testMultiplication(self):
		self.assertEqual(Roman("III")*Roman("II"), "VI")

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
