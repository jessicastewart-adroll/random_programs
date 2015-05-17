class Roman(object):
	def __init__(self, roman):
		self.roman = roman
		self.romans_int = self.convert_to_int(self.roman) 

	def convert_to_int(self, roman):
		roman_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		i = 0
		j = i+1
		result = 0

		while j < len(roman)-1:
			if roman_to_int[i] >= roman_to_int[j]:
				result += roman_to_int[i]
				i += 1
				j += 1
			else:
				result += roman_to_int[j] - roman_to_int[i]
				i += 2
				j += 2

		return result

	def convert_int_to_roman(self, number):
		tens = 'IXCM'
		fives = 'VLD'
		num = [int(i) for i in str(number)]
		result = []
		notation = len(str(number))
		i = 0

		while notation >= 0:
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
			else num[i] == 9:
				result.extend((tens[notation], tens[notation+1]))
				i += 1
				notation -= 1

		return ''.join(result)

	def __add__(self, other):
		return convert_int_to_roman(self.romans_int + other.romans_int)

	def __sub__(self, other):
		return convert_int_to_roman(self.romans_int - other.romans_int)

	def __mul__(self, other):
		return convert_int_to_roman(self.romans_int * other.romans_int)

	def __eq__(self, other):
		return self.romans_int == other.romans_int

	def __ne__(self, other):
		return self.romans_int != other.romans_int
