"""Roman numeral calculator

Interface: 
Roman.new("V") + Roman.new("IV") => Roman.new("IX")
methods: +, -, *, ==  (don't need to go into fractions/decimals with division). 

Think about how you would organize your code, as well as what other methods would be logical for an end user to expect. 
If you have tests or can make this into a command like program that would be even better. 
"""

class Roman(object):
	def __init__(self, roman):
		self.roman = roman
		self.romans_int = self.convert_to_int(self.roman) 

	def convert_to_int(self, roman):
		roman_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		i = 0
		j = i+1
		result = 0

		while i < len(roman):
			if j == len(roman):
				result += roman_to_int[roman[i]]
				i += 1
			elif roman_to_int[roman[i]] >= roman_to_int[roman[j]]:
				result += roman_to_int[roman[i]]
				i += 1
				j += 1
			else:
				result += roman_to_int[roman[j]] - roman_to_int[roman[i]]
				i += 2
				j += 2

		return result

	def convert_to_roman(self, number):
		tens = 'IXCM'
		fives = 'VLD'
		num = [int(n) for n in str(number)]
		result = []
		notation = len(num)-1
		i = 0

		while i < len(num):
			if num[i] == 0:
				i += 1
				notation -= 1
			elif num[i] >= 1 and num[i] <= 3:
				result.append(tens[notation]*num[i]) 
				i += 1
				notation -= 1
			elif num[i] >= 6 and num[i] <= 8:
				result.extend((fives[notation], tens[notation]*(num[i]-5))) 
				i += 1
				notation -= 1
			elif num[i] == 5:
				result.append(fives[notation])
				i += 1
				notation -= 1
			elif num[i] == 4:
				result.extend((tens[notation], fives[notation]))
				i += 1
				notation -= 1
			else:
				result.extend((tens[notation], tens[notation+1]))
				i += 1
				notation -= 1

		return ''.join(result)

	def __add__(self, other):
		return self.convert_to_roman(self.romans_int + other.romans_int)

	def __sub__(self, other):
		return self.convert_to_roman(self.romans_int - other.romans_int)

	def __mul__(self, other):
		return self.convert_to_roman(self.romans_int * other.romans_int)

	def __eq__(self, other):
		return self.romans_int == other.romans_int

	def __ne__(self, other):
		return self.romans_int != other.romans_int
