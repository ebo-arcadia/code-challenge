# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the
# API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and
# skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in
# MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000

# Help
# Symbol	Value
# I	1
# IV 4
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# pseudocode
# method 1
# compare the given num with the base num in the roman numerals dictionary
# divide the number by the corresponding base num times the quotient num of times
# recursively execute the same operation to the reminder till the given num becomes zero
# method 2
# the first digit is considered as the significant num
# set a divisor such as 1000, 100, 10, 1
# divide the given number with the corresponding divisor
# extract the significant num
# find corresponding roman char as value per significant num as the key
# conditionally append roman char

import math


class RomanNumerals:

    @staticmethod
    def to_roman(numeral):
        numerals_roman_dict = \
            {
                1: "I",
                4: "IV",
                5: "V",
                9: "IX",
                10: "X",
                40: "XL",
                50: "L",
                90: "XC",
                100: "C",
                400: "CD",
                500: "D",
                900: "CM",
                1000: "M"
            }

        divisor = 1
        while numeral >= divisor:
            # divisor = (divisor * (10 ** len(str(numeral)))) / 10
            # significant_num = int(numeral / divisor)
            # print(significant_num)
            # floated = float(numeral / divisor)
            # reminder = round(floated - significant_num, len(str(numeral)))
            # print(reminder)
            # divisor = divisor / 10
            # numeral = reminder * divisor * 10
            # print(numeral)
            divisor *= 10
        divisor /= 10

        result = ""

        while numeral:
            significant_num = int(numeral / divisor)  # extract significant number
            # if significant_num in roman_numerals_dict.keys():
            #     result += roman_numerals_dict[significant_num]

            if significant_num <= 3:
                result += numerals_roman_dict[divisor] * significant_num

            elif significant_num == 4:
                result += numerals_roman_dict[divisor] + numerals_roman_dict[divisor * 5]

            elif 5 <= significant_num <= 8:
                result += numerals_roman_dict[divisor * 5] + numerals_roman_dict[divisor] * (significant_num - 5)

            elif significant_num == 9:
                result += numerals_roman_dict[divisor] + numerals_roman_dict[divisor * 10]

            else:
                return "out of range"

            numeral = math.floor(numeral % divisor)
            divisor /= 10

        return result


    def int_to_roman_two_lists(self, num):
        numerals_map = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''

        counter = 0
        while num > 0:
            for i in range(num // numerals_map[counter]):
                result += roman_char[counter]
                num -= numerals_map[counter]
            counter += 1
        return result

    def int_to_roman_loop_over_pairs(self, num):
        numerals_roman_pairs = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        result = ''

        while num > 0:
            for numeral, roman_char in numerals_roman_pairs:
                while num >= numeral:
                    result += roman_char
                    num -= numeral
        return result

    def roman_to_it(self, roman):
        roman_numerals_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        converted_num = 0
        roman = roman.replace("IV", "IIII").replace("IX", "VIIII")
        roman = roman.replace("XL", "XXXX").replace("XC", "LXXXX")
        roman = roman.replace("CD", "CCCC").replace("CM", "DCCCC")

        for character in roman:
            converted_num += roman_numerals_dict[character]
        return converted_num


roman_numerals = RomanNumerals()
print("-----------------------")
print("testing to_roman: ")
print("-----------------------")
print(roman_numerals.to_roman(1))
print(roman_numerals.to_roman(2))
print(roman_numerals.to_roman(4))
print(roman_numerals.to_roman(5))
print(roman_numerals.to_roman(6))
print(roman_numerals.to_roman(7))
print(roman_numerals.to_roman(8))
print(roman_numerals.to_roman(9))
print(roman_numerals.to_roman(10))
print(roman_numerals.to_roman(21))
print(roman_numerals.to_roman(40))
print(roman_numerals.to_roman(123))
print(roman_numerals.to_roman(1000))
print(roman_numerals.to_roman(1990))
print(roman_numerals.to_roman(3213))
print("======================")
print("testing int_to_roman_two_lists method: ")
print(roman_numerals.int_to_roman_two_lists(3213))
print("======================")
print("testing int_to_roman_loop_over_pairs method: ")
print(roman_numerals.int_to_roman_loop_over_pairs(321))
print("======================")
print("testing roman_to_int method: ")
print(roman_numerals.roman_to_it("I"))
print(roman_numerals.roman_to_it("IV"))
print(roman_numerals.roman_to_it("IX"))
print(roman_numerals.roman_to_it("XLXLXL"))
print(roman_numerals.roman_to_it("XCXXX"))
print(roman_numerals.roman_to_it("CMCDCM"))
