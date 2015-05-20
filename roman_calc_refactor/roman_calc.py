"""
Refactored for readability
  extending use of dictionary lookups (due to limited scale of Roman numerals) rather than runtime math
  to_roman: arithmetic operations on input number rather than converting input to sequence 
"""

class Roman(object):
    def __init__(self, roman):
        self.roman = roman
        self.roman_int = self.__int__()

    def __int__(self):
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        #  hardcoding 4's and 9's for readability
        i = 0
        result = 0

        while i < len(self.roman):
            if (i+1) == len(self.roman):
                result += roman_dict[self.roman[i]]
                break
                #  handles last item of sequence
                #  if no successive, add then break
            elif roman_dict[self.roman[i]] >= roman_dict[self.roman[i+1]]:
                result += roman_dict[self.roman[i]]
                i += 1
            elif roman_dict[self.roman[i]] <= roman_dict[self.roman[i+1]]:
                result += roman_dict[self.roman[i+1]] - roman_dict[self.roman[i]]
                i += 2

        return result

    def to_roman(self, number):
        thousands = {1: "M", 2: "MM", 3: "MMM"}
        hundreds = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D",
        600: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        tens = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        ones = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}

        result = ""

        if number >= 1000:  #  confirm value in this notation
            result += thousands[number/1000]    #  use division (integer) to get exact number
            number = number%1000    # overwrite variable with number is next notation using modulus

        if number < 1000 and number >= 100:
            result += hundreds[number/100]
            number = number%100

        if number < 100 and number >= 10:
            result += tens[number/10]
            number = number%10

        if number:
            result += ones[number]

        return Roman(result)

    def __add__(self, other):
        return self.to_roman(self.roman_int + other.roman_int)

    def __sub__(self, other):
        return self.to_roman(self.roman_int - other.roman_int)

    def __mul__(self, other):
        return self.to_roman(self.roman_int * other.roman_int)

    def __eq__(self, other):
        return self.roman == other.roman

    def __ne__(self, other):
        return self.roman != other.roman
